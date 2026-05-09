#!/usr/bin/env bash
set -euo pipefail

HOST="codex"
PERSIST_SHELL=0
DRY_RUN=0
ADVANCED_EXA_URL="https://mcp.exa.ai/mcp?tools=web_search_exa,web_fetch_exa,web_search_advanced_exa"
WEBSETS_URL="https://websetsmcp.exa.ai/mcp"

usage() {
  cat <<'USAGE'
Usage: setup_exa_connectors.sh [--host codex|claude] [--persist-shell] [--dry-run]

Prompts for EXA_API_KEY when it is not already set, writes a local env file,
and configures Exa/Websets MCP entries for the selected host when the CLI exists.

Examples:
  plugins/gtm-agent/scripts/setup_exa_connectors.sh --host codex --persist-shell
  EXA_API_KEY=... plugins/gtm-agent/scripts/setup_exa_connectors.sh --host claude
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --host)
      HOST="${2:-}"
      shift 2
      ;;
    --persist-shell)
      PERSIST_SHELL=1
      shift
      ;;
    --dry-run)
      DRY_RUN=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if [[ "$HOST" != "codex" && "$HOST" != "claude" ]]; then
  echo "--host must be codex or claude" >&2
  exit 2
fi

if [[ -z "${EXA_API_KEY:-}" ]]; then
  if [[ -t 0 ]]; then
    printf "Open https://dashboard.exa.ai/api-keys, create a key, then paste it here.\n" >&2
    read -r -s -p "Exa API key: " EXA_API_KEY
    printf "\n" >&2
  else
    echo "EXA_API_KEY is not set and stdin is not interactive." >&2
    exit 2
  fi
fi

if [[ -z "$EXA_API_KEY" ]]; then
  echo "EXA_API_KEY cannot be empty." >&2
  exit 2
fi

CONFIG_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/mem-plugins/gtm-agent"
ENV_FILE="$CONFIG_DIR/exa.env"
if [[ "$DRY_RUN" == "1" ]]; then
  echo "DRY RUN: would write $ENV_FILE with 0600 permissions"
else
  mkdir -p "$CONFIG_DIR"
  umask 077
  printf 'export EXA_API_KEY=%q\n' "$EXA_API_KEY" > "$ENV_FILE"
  chmod 600 "$ENV_FILE"
fi
export EXA_API_KEY

if [[ "$PERSIST_SHELL" == "1" ]]; then
  PROFILE="${SHELL_PROFILE:-$HOME/.zshrc}"
  SOURCE_LINE="source \"$ENV_FILE\""
  if [[ "$DRY_RUN" == "1" ]]; then
    echo "DRY RUN: would append source line to $PROFILE"
  else
    touch "$PROFILE"
    if ! grep -Fq "$SOURCE_LINE" "$PROFILE"; then
      printf '\n# mem-plugins GTM Agent Exa key\n%s\n' "$SOURCE_LINE" >> "$PROFILE"
    fi
  fi
fi

run_cmd() {
  if [[ "$DRY_RUN" == "1" ]]; then
    printf 'DRY RUN:'
    for arg in "$@"; do
      safe_arg="${arg//$EXA_API_KEY/REDACTED_EXA_API_KEY}"
      printf ' %q' "$safe_arg"
    done
    printf '\n'
  else
    "$@"
  fi
}

if [[ "$HOST" == "codex" ]]; then
  if command -v codex >/dev/null 2>&1; then
    run_cmd codex mcp add exa --url "${ADVANCED_EXA_URL}&exaApiKey=${EXA_API_KEY}" || true
    run_cmd codex mcp add websets --url "$WEBSETS_URL" --bearer-token-env-var EXA_API_KEY || true
  else
    echo "codex CLI not found; wrote $ENV_FILE only." >&2
  fi
elif [[ "$HOST" == "claude" ]]; then
  if command -v claude >/dev/null 2>&1; then
    run_cmd claude mcp add --transport http exa "$ADVANCED_EXA_URL" --header "x-api-key: $EXA_API_KEY" || true
    run_cmd claude mcp add --transport http websets "$WEBSETS_URL" --header "Authorization: Bearer $EXA_API_KEY" || true
  else
    echo "claude CLI not found; wrote $ENV_FILE only." >&2
  fi
fi

cat <<EOF
Exa key setup complete for $HOST.
Env file: $ENV_FILE
Reload/restart the host, then verify:
- web_search_advanced_exa is available for company, people, article/news searches
- Websets tools are available for persistent company/person sourcing
EOF
