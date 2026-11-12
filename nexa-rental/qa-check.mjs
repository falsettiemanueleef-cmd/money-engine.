import fs from "node:fs";
import vm from "node:vm";
import assert from "node:assert/strict";

const root = new URL(".", import.meta.url);
const html = fs.readFileSync(new URL("index.html", root), "utf8");
const sw = fs.readFileSync(new URL("sw.js", root), "utf8");
const manifestText = fs.readFileSync(new URL("manifest.webmanifest", root), "utf8");

const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/gi)];
assert.equal(scripts.length, 1, "Expected exactly one inline application script");
new vm.Script(scripts[0][1], { filename: "index.html:inline-script" });
new vm.Script(sw, { filename: "sw.js" });

const manifest = JSON.parse(manifestText);
assert.equal(manifest.name, "NEXA Rental Profit Manager");
assert.equal(manifest.display, "standalone");
assert.ok(manifest.start_url && manifest.scope, "PWA start_url/scope must exist");

const wordsMatch = html.match(/const words=(\{[\s\S]*?\n\});\nlet lang/);
assert.ok(wordsMatch, "Could not locate translation dictionaries");
const dictionaries = vm.runInNewContext("(" + wordsMatch[1] + ")");
const languages = ["it", "en", "es", "fr", "de"];
for (const language of languages) {
  assert.ok(dictionaries[language], "Missing language dictionary: " + language);
}
const baseKeys = Object.keys(dictionaries.it).sort();
for (const language of languages.slice(1)) {
  const keys = Object.keys(dictionaries[language]).sort();
  const missing = baseKeys.filter(key => !keys.includes(key));
  const extra = keys.filter(key => !baseKeys.includes(key));
  assert.deepEqual({ missing, extra }, { missing: [], extra: [] },
    "Translation key mismatch for " + language);
}

const ids = [...html.matchAll(/\bid="([^"]+)"/g)].map(match => match[1]);
const duplicates = ids.filter((id, index) => ids.indexOf(id) !== index);
assert.deepEqual([...new Set(duplicates)], [], "Duplicate static HTML IDs found");
for (const required of ["lang", "tabs", "notice", "app", "manifest.webmanifest"]) {
  assert.ok(html.includes(required), "Missing required app/PWA element: " + required);
}
assert.ok(sw.includes("./index.html"), "Service worker must cache the app shell");

for (const required of ["function calendarPage()", "function overlapExists(", "data-er=", "data-ee=", "function reportPage()", "revpar", "avgStay"]) {
  assert.ok(html.includes(required), "Missing expected product feature: " + required);
}
for (const language of languages) {
  assert.ok(html.includes("Object.assign(words." + language), "Missing extended translations for " + language);
}
assert.ok(html.includes("data-map"), "CSV column mapping must remain available");
assert.ok(html.includes("localStorage.setItem"), "Local persistence must remain available");
assert.ok(html.includes('id="exportExpenses"'), "Expense CSV export must be available");
assert.ok(html.includes("function validISO("), "Strict ISO date validation must be available");
assert.ok(html.includes("overlapExists(candidate)"), "CSV imports must reject overlapping reservations");
assert.ok(html.includes('name="currency"'), "Expenses must support an explicit currency");

console.log("PASS: inline JavaScript syntax");
console.log("PASS: service worker JavaScript syntax");
console.log("PASS: PWA manifest JSON and standalone configuration");
console.log("PASS: all five translation dictionaries have matching keys (" + baseKeys.length + ")");
console.log("PASS: no duplicate static HTML IDs");
console.log("LIMIT: static checks only; no browser interaction, device, import fixture, or financial calculation tests were run.");
