# HUMA629 REAL TOKENS - VAULTS - TEST ONLY
# PUF 368F9466 CHAIN 629 - NO REAL WALLET - NO PASSPHRASE YET
import hashlib, json, os
PUF = "368F9466"
TOKENS_42_REAL = [
"Ringcoin",
"Atom",
"Meteorite",
"Photon",
"Diamond",
"Gold",
"Platinum",
"Lithium",
"Uranium",
"Quartz",
"Water",
"Oil",
"Solar",
"Pulse",
"Tribute",
"Silver",
"Copper",
"Iron",
"Nickel",
"Cobalt",
"Zinc",
"Tin",
"Lead",
"Aluminium",
"Bronze",
"Brass",
"Steel",
"Coal",
"Gas",
"Hydrogen",
"Oxygen",
"Carbon",
"Nitrogen",
"Helium",
"Neon",
"Titanium",
"Chromium",
"Manganese",
"Mercury",
"Emerald",
"Ruby",
"Sapphire",
"Topaz",
"Jade",
"Pearl",
"Coral",
"Amber",
"Liquidity-HUMA",
"Liquidity-HGN",
"Liquidity-Pi",
]
print(f"Total: {len(TOKENS_42_REAL)}")
out_dir = os.path.expanduser("~/hgn_new_7/VAULTS_42_TOKENS_REAL")
os.makedirs(out_dir, exist_ok=True)
wallets = []
for i, token in enumerate(TOKENS_42_REAL, 1):
    test_seed = hashlib.sha256(f"TEST-REAL-{token}-{PUF}-42".encode()).hexdigest()
    secret_test = hashlib.sha256(f"TEST-SECRET-{test_seed}".encode()).hexdigest()
    public_test = "huma629" + hashlib.sha256(secret_test.encode()).hexdigest()[:38]
    vault_key_test = hashlib.sha256(f"TEST-VAULT-{secret_test}".encode()).hexdigest()[:32]
    locker_key_test = hashlib.sha256(f"TEST-LOCKER-{secret_test}".encode()).hexdigest()[:32]
    wallets.append({"no": i, "token": token, "mode": "TEST - NO REAL WALLET - NO PASSPHRASE YET", "keypair_secret_test": secret_test, "keypair_public_huma629": public_test, "vault_key_test": vault_key_test, "locker_key_test": locker_key_test, "qr_address": public_test, "barcode_address": public_test, "passphrase": "", "mnemonic": "", "vault": f"VAULT_{token}", "locker": f"LOCKER_{token}"})
    print(f"{i:02d}. {token:20s} VAULT={public_test} | Passphrase: [EMPTY] | TEST")
with open(os.path.join(out_dir, "42_TOKENS_REAL_VAULTS_TEST.json"), "w") as f:
    json.dump(wallets, f, indent=2)
print(f"Saved: {out_dir}/42_TOKENS_REAL_VAULTS_TEST.json")
print("TEST ONLY - HUMA ONLY - NO REAL WALLET")
