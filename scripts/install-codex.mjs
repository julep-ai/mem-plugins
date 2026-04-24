#!/usr/bin/env node
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

const dryRun = process.argv.includes("--dry-run");
const pluginName = "content-lead";
const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(scriptDir, "..");
const pluginSource = path.join(repoRoot, "plugins", pluginName);
const home = os.homedir();
const userPluginsDir = path.join(home, "plugins");
const userAgentsPluginsDir = path.join(home, ".agents", "plugins");
const pluginTarget = path.join(userPluginsDir, pluginName);
const marketplacePath = path.join(userAgentsPluginsDir, "marketplace.json");

function writeJson(filePath, payload) {
  const body = `${JSON.stringify(payload, null, 2)}\n`;
  if (dryRun) {
    console.log(`[dry-run] write ${filePath}`);
    console.log(body);
    return;
  }
  fs.mkdirSync(path.dirname(filePath), { recursive: true });
  fs.writeFileSync(filePath, body);
}

function readMarketplace() {
  if (!fs.existsSync(marketplacePath)) {
    return {
      name: "local",
      interface: {
        displayName: "Local Plugins",
      },
      plugins: [],
    };
  }

  return JSON.parse(fs.readFileSync(marketplacePath, "utf8"));
}

function installSymlink() {
  if (dryRun) {
    console.log(`[dry-run] ensure ${userPluginsDir}`);
    console.log(`[dry-run] symlink ${pluginTarget} -> ${pluginSource}`);
    return;
  }

  fs.mkdirSync(userPluginsDir, { recursive: true });
  if (fs.existsSync(pluginTarget)) {
    const existing = fs.lstatSync(pluginTarget);
    if (!existing.isSymbolicLink()) {
      console.error(`Refusing to replace non-symlink path: ${pluginTarget}`);
      process.exit(1);
    }
    fs.unlinkSync(pluginTarget);
  }
  fs.symlinkSync(pluginSource, pluginTarget, "dir");
}

function installMarketplaceEntry() {
  const marketplace = readMarketplace();
  marketplace.name ??= "local";
  marketplace.interface ??= { displayName: "Local Plugins" };
  marketplace.plugins ??= [];

  const entry = {
    name: pluginName,
    source: {
      source: "local",
      path: `./plugins/${pluginName}`,
    },
    policy: {
      installation: "AVAILABLE",
      authentication: "ON_INSTALL",
    },
    category: "Productivity",
  };

  const existingIndex = marketplace.plugins.findIndex((item) => item?.name === pluginName);
  if (existingIndex >= 0) {
    marketplace.plugins[existingIndex] = entry;
  } else {
    marketplace.plugins.push(entry);
  }

  writeJson(marketplacePath, marketplace);
}

if (!fs.existsSync(pluginSource)) {
  console.error(`Plugin source not found: ${pluginSource}`);
  process.exit(1);
}

installSymlink();
installMarketplaceEntry();

console.log(dryRun ? `${pluginName} install preview complete.` : `${pluginName} installed for Codex.`);
console.log("Restart Codex, then complete Memory Store MCP auth when prompted.");
