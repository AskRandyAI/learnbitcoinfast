from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent
SITE = "https://www.learnbitcoinfast.com"
TODAY = "2026-08-25"

NAV = [
    ("Blog Posts", "/blog/"),
    ("Free book", "/book/"),
    ("Start here", "/start.html"),
    ("About", "/about.html"),
]

POSTS = [
    {
        "slug": "what-is-bitcoin",
        "title": "What Is Bitcoin? A Clear Beginner Explanation",
        "desc": "Learn what Bitcoin is, how it works, why it was created, and how it differs from regular money — in plain English.",
        "date": "2026-08-25",
        "read": "8 min",
        "kw": "what is bitcoin, bitcoin explained, bitcoin for beginners",
        "h1": "What is Bitcoin?",
    },
    {
        "slug": "how-to-buy-bitcoin",
        "title": "How to Buy Bitcoin as a Beginner",
        "desc": "A step-by-step guide to buying Bitcoin safely: accounts, funding, first purchase, and moving coins off an exchange.",
        "date": "2026-08-25",
        "read": "9 min",
        "kw": "how to buy bitcoin, buy bitcoin for beginners",
        "h1": "How to buy Bitcoin",
    },
    {
        "slug": "bitcoin-wallet-for-beginners",
        "title": "Bitcoin Wallet for Beginners: Hot vs Cold Storage",
        "desc": "Understand Bitcoin wallets, seed phrases, hot wallets, and hardware wallets before you store any coins.",
        "date": "2026-08-25",
        "read": "8 min",
        "kw": "bitcoin wallet, bitcoin wallet for beginners, seed phrase",
        "h1": "Bitcoin wallets for beginners",
    },
    {
        "slug": "how-to-store-bitcoin-safely",
        "title": "How to Store Bitcoin Safely (Self-Custody Basics)",
        "desc": "Learn self-custody: backups, seed phrases, hardware wallets, and the mistakes that lose Bitcoin forever.",
        "date": "2026-08-25",
        "read": "9 min",
        "kw": "how to store bitcoin, bitcoin self custody, bitcoin security",
        "h1": "How to store Bitcoin safely",
    },
    {
        "slug": "bitcoin-vs-crypto",
        "title": "Bitcoin vs Crypto: Why They Are Not the Same",
        "desc": "Bitcoin is not “crypto.” Learn the difference, why it matters, and what beginners should ignore.",
        "date": "2026-08-25",
        "read": "7 min",
        "kw": "bitcoin vs crypto, bitcoin vs altcoins",
        "h1": "Bitcoin vs crypto",
    },
    {
        "slug": "how-bitcoin-mining-works",
        "title": "How Bitcoin Mining Works (Without the Jargon)",
        "desc": "A simple explanation of Bitcoin mining, blocks, energy, and why miners exist.",
        "date": "2026-08-25",
        "read": "8 min",
        "kw": "how bitcoin mining works, bitcoin mining explained",
        "h1": "How Bitcoin mining works",
    },
    {
        "slug": "dollar-cost-averaging-bitcoin",
        "title": "Dollar-Cost Averaging Bitcoin: A Simple Strategy",
        "desc": "How DCA works for Bitcoin, why beginners use it, and what it does not guarantee.",
        "date": "2026-08-25",
        "read": "7 min",
        "kw": "dollar cost averaging bitcoin, dca bitcoin",
        "h1": "Dollar-cost averaging Bitcoin",
    },
    {
        "slug": "bitcoin-glossary",
        "title": "Bitcoin Glossary: 30 Terms Beginners Actually Need",
        "desc": "A practical Bitcoin glossary covering sats, wallets, keys, nodes, fees, and more.",
        "date": "2026-08-25",
        "read": "10 min",
        "kw": "bitcoin glossary, bitcoin terms",
        "h1": "Bitcoin glossary",
    },
]


def head(title, desc, path, type_="website", extra=""):
    url = SITE + path
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{url}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta property="og:type" content="{type_}">
  <meta property="og:site_name" content="Learn Bitcoin Fast">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="theme-color" content="#0b1a3a">
  <link rel="stylesheet" href="/css/site.css">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1465049145329243"
     crossorigin="anonymous"></script>
  {extra}
</head>"""


def chrome(active=None):
    links = []
    for label, href in NAV:
        cls = ' class="active"' if active == href else ""
        links.append(f'<a href="{href}"{cls}>{label}</a>')
    return f"""
<body>
  <header class="site-header">
    <div class="wrap">
      <a class="logo" href="/"><span class="mark">₿</span> Learn Bitcoin Fast</a>
      <nav>{''.join(links)}</nav>
    </div>
  </header>
"""


FOOT = """
  <footer class="site-footer">
    <div class="wrap">
      <p><strong>Learn Bitcoin Fast</strong> · Education only. Not financial, tax, or legal advice. Bitcoin is volatile. Never invest money you cannot afford to lose.</p>
      <p><a href="/start.html">Start here</a> · <a href="/book/">Free book</a> · <a href="/blog/">Blog</a> · <a href="/about.html">About</a> · <a href="/privacy.html">Privacy</a> · <a href="/contact.html">Contact</a></p>
      <p>© Learn Bitcoin Fast</p>
    </div>
  </footer>
</body>
</html>
"""


def page(title, desc, path, body, active=None, type_="website", extra=""):
    return head(title, desc, path, type_, extra) + chrome(active) + body + FOOT


def write(rel, html):
    p = ROOT / rel.lstrip("/")
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html, encoding="utf-8")
    print("wrote", rel)


org = """<script type="application/ld+json">{"@context":"https://schema.org","@type":"Organization","name":"Learn Bitcoin Fast","url":"https://www.learnbitcoinfast.com","description":"Beginner Bitcoin education: wallets, self-custody, and how Bitcoin works."}</script>"""

index_body = """
  <main>
    <section class="hero">
      <div class="wrap">
        <p class="kicker">The Bitcoin Blueprint</p>
        <h1>Learn Bitcoin Fast</h1>
        <p class="lede">A concise beginner’s book: what Bitcoin is, why it matters, and how to buy and self-custody it. Turn the pages like a real book.</p>
        <div class="hero-actions">
          <a class="btn btn-orange" href="/book/read/">Read the free book</a>
          <a class="btn" href="/book/">About the book</a>
        </div>
      </div>
    </section>
    <section>
      <div class="wrap grid-3">
        <article class="card"><p class="kicker">01</p><h2>Fundamentals</h2><p>What Bitcoin is, why it was created, and how it differs from banks and “crypto.”</p></article>
        <article class="card"><p class="kicker">02</p><h2>Security</h2><p>Wallets, private keys, seed phrases, and cold storage — without the panic.</p></article>
        <article class="card"><p class="kicker">03</p><h2>Long-term</h2><p>How to buy carefully, take self-custody, and think in years instead of days.</p></article>
      </div>
    </section>
  </main>
"""
write("index.html", page(
    "Learn Bitcoin Fast | Beginner Bitcoin Guides",
    "Learn Bitcoin fast with clear beginner guides: what Bitcoin is, how to buy it, wallets, self-custody, and mining — no hype.",
    "/",
    index_body,
    extra=org,
))

start_body = """
  <main class="wrap" style="padding:3rem 0">
    <p class="kicker">Curriculum</p>
    <h1>Start here</h1>
    <p class="lede">Follow this order. Each lesson builds on the last. Skip the price charts until you understand wallets.</p>
    <ol class="prose">
      <li><a href="/blog/what-is-bitcoin.html">What is Bitcoin?</a></li>
      <li><a href="/blog/bitcoin-vs-crypto.html">Bitcoin vs crypto</a></li>
      <li><a href="/blog/bitcoin-wallet-for-beginners.html">Wallets and seed phrases</a></li>
      <li><a href="/blog/how-to-buy-bitcoin.html">How to buy Bitcoin</a></li>
      <li><a href="/blog/how-to-store-bitcoin-safely.html">How to store it safely</a></li>
      <li><a href="/blog/dollar-cost-averaging-bitcoin.html">A simple buying habit</a></li>
      <li><a href="/blog/how-bitcoin-mining-works.html">How mining works</a></li>
      <li><a href="/blog/bitcoin-glossary.html">Glossary</a></li>
    </ol>
  </main>
"""
write("start.html", page(
    "Start Here | Learn Bitcoin Fast",
    "A step-by-step Bitcoin beginner path: what Bitcoin is, wallets, buying, self-custody, and mining.",
    "/start.html",
    start_body,
    "/start.html",
))

about_body = """
  <main class="wrap prose" style="padding:3rem 0">
    <p class="kicker">About</p>
    <h1>About Learn Bitcoin Fast</h1>
    <p>Most Bitcoin content is either a sales pitch or a whitepaper. This site is the middle: short, accurate lessons so a complete beginner can understand Bitcoin in a weekend — then keep learning.</p>
    <p>We cover Bitcoin only. Not token casinos, not trading signals, not “AI robots.” Education. You still have to do your own research.</p>
    <p>Questions: <a href="/contact.html">contact</a>.</p>
  </main>
"""
write("about.html", page(
    "About | Learn Bitcoin Fast",
    "Learn Bitcoin Fast is a beginner Bitcoin education site: clear lessons on wallets, buying, and self-custody.",
    "/about.html",
    about_body,
    "/about.html",
))

contact_body = """
  <main class="wrap prose" style="padding:3rem 0">
    <h1>Contact</h1>
    <p>Email <a href="mailto:hello@learnbitcoinfast.com">hello@learnbitcoinfast.com</a> for corrections, guest posts, or questions about the guides.</p>
  </main>
"""
write("contact.html", page(
    "Contact | Learn Bitcoin Fast",
    "Contact Learn Bitcoin Fast.",
    "/contact.html",
    contact_body,
))

privacy_body = """
  <main class="wrap prose" style="padding:3rem 0">
    <h1>Privacy Policy</h1>
    <p>Last updated: August 26, 2026</p>
    <p>Learn Bitcoin Fast (“we”) operates https://www.learnbitcoinfast.com. This policy explains what information may be collected when you use the site, including through Google AdSense advertising.</p>
    <h2>Information we collect</h2>
    <p>We do not require an account. Our web host may automatically collect standard server logs such as IP address, browser type, and pages visited.</p>
    <h2>Google AdSense and cookies</h2>
    <p>We use Google AdSense to show ads. Google and its partners use cookies and similar technologies to serve ads based on your prior visits to this site and other sites. Google’s use of advertising cookies enables it and its partners to serve ads based on your visit to this site and/or other sites on the Internet.</p>
    <p>You may opt out of personalized advertising by visiting <a href="https://www.google.com/settings/ads" rel="noopener">Google Ads Settings</a>. You can also opt out of some third-party vendors’ use of cookies for personalized advertising at <a href="https://www.aboutads.info/choices/" rel="noopener">www.aboutads.info/choices</a>.</p>
    <p>Third-party vendors, including Google, use cookies to serve ads based on a user’s prior visits. For more information about how Google uses data, see <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">How Google uses information from sites or apps that use our services</a>.</p>
    <h2>How we use information</h2>
    <p>Logs and advertising data may be used to operate the site, measure traffic, and display ads. We do not sell your personal information.</p>
    <h2>Children</h2>
    <p>This site is not directed at children under 13. We do not knowingly collect personal information from children.</p>
    <h2>Contact</h2>
    <p>Questions: <a href="mailto:hello@learnbitcoinfast.com">hello@learnbitcoinfast.com</a></p>
  </main>
"""
write("privacy.html", page(
    "Privacy Policy | Learn Bitcoin Fast",
    "Privacy policy for Learn Bitcoin Fast, including Google AdSense cookies, ads, and how to opt out of personalized advertising.",
    "/privacy.html",
    privacy_body,
))

blog_index = f"""
  <main class="wrap" style="padding:3rem 0">
    <p class="kicker">Blog Posts</p>
    <h1>Blog Posts</h1>
    <p class="lede">Beginner articles written to rank and to teach. Start with what Bitcoin is, then wallets, then buying.</p>
    <div class="grid-2" style="margin-top:1.5rem">
      {''.join(f'<a class="card block" href="/blog/{p["slug"]}.html"><p class="meta">{p["date"]} · {p["read"]}</p><h2>{p["h1"]}</h2><p>{p["desc"]}</p></a>' for p in POSTS)}
    </div>
  </main>
"""
write("blog/index.html", page(
    "Bitcoin Blog for Beginners | Learn Bitcoin Fast",
    "Beginner Bitcoin blog: what Bitcoin is, how to buy Bitcoin, wallets, self-custody, mining, and a glossary.",
    "/blog/",
    blog_index,
    "/blog/",
))

book_body = """
  <main class="wrap" style="padding:3.5rem 0">
    <p class="kicker">Free book</p>
    <h1>Bitcoin Blueprint</h1>
    <p class="lede">A concise beginner’s guide that explains what Bitcoin is, why it matters, and how to safely buy and self-custody it.</p>
    <div class="card" style="margin:1.5rem 0;max-width:40rem">
      <p>Inside you’ll find clear lessons on fundamentals, security, buying strategies, and long-term thinking — designed to help you move from confusion to confidence.</p>
      <ul>
        <li>What Bitcoin is and why it exists</li>
        <li>Wallets, keys, and seed phrases</li>
        <li>How to buy without getting trapped on an exchange</li>
        <li>Self-custody and cold storage</li>
        <li>A simple long-term habit (DCA)</li>
      </ul>
      <div class="hero-actions">
        <a class="btn btn-orange" href="/book/read/">Read the book</a>
        <a class="btn" href="/">Back home</a>
      </div>
    </div>
    <p class="fine">Start your Bitcoin journey today. Education only. Not financial advice.</p>
  </main>
"""
write("book/index.html", page(
    "Bitcoin Blueprint (Free Book) | Learn Bitcoin Fast",
    "Read the free Bitcoin Blueprint: a beginner’s guide to what Bitcoin is, how to buy it, and how to self-custody it.",
    "/book/",
    book_body,
    "/book/",
    extra='<script type="application/ld+json">{"@context":"https://schema.org","@type":"Book","name":"Bitcoin Blueprint","author":{"@type":"Organization","name":"Learn Bitcoin Fast"},"url":"https://www.learnbitcoinfast.com/book/","description":"A concise beginner guide to Bitcoin: fundamentals, security, buying, and self-custody."}</script>',
))

chapters = [
    ("what-is-bitcoin", "Chapter 1 · What Bitcoin is"),
    ("bitcoin-vs-crypto", "Chapter 2 · Bitcoin vs crypto"),
    ("bitcoin-wallet-for-beginners", "Chapter 3 · Wallets"),
    ("how-to-buy-bitcoin", "Chapter 4 · How to buy"),
    ("how-to-store-bitcoin-safely", "Chapter 5 · How to store it"),
    ("dollar-cost-averaging-bitcoin", "Chapter 6 · Long-term habit"),
    ("how-bitcoin-mining-works", "Chapter 7 · Mining"),
    ("bitcoin-glossary", "Chapter 8 · Glossary"),
]
# book/read is generated after BODIES exist

BODIES = {}

BODIES["what-is-bitcoin"] = """
<p>Bitcoin is digital money that no bank or government issues. It runs on a public network of computers. Anyone can send value to anyone else, as long as both sides can use the Bitcoin network.</p>
<p>That is the whole idea. The rest is how it stays honest without a central company in charge.</p>
<h2>Why Bitcoin exists</h2>
<p>Bitcoin launched in 2009 after the 2008 financial crisis. The creator used the name Satoshi Nakamoto. The design problem was simple and hard: how do you transfer money on the internet without trusting a bank, and without letting people spend the same coins twice?</p>
<p>Bitcoin’s answer is a public ledger called the blockchain, plus mining, plus a hard cap of 21 million coins.</p>
<h2>How it works in one minute</h2>
<ul>
<li>You hold Bitcoin with a wallet and keys, not a username at a bank.</li>
<li>A transaction is a signed message: “send this amount to that address.”</li>
<li>Miners compete to add batches of transactions (blocks) to the chain.</li>
<li>The network agrees on one history. Changing old blocks is extremely expensive.</li>
</ul>
<p>You do not need to run a miner to use Bitcoin. You need a wallet, a small amount of Bitcoin, and a basic security habit. Read <a href="/blog/bitcoin-wallet-for-beginners.html">wallets for beginners</a> next.</p>
<h2>Bitcoin is not a company</h2>
<p>There is no Bitcoin Inc. that can freeze your coins because a support ticket failed. That is freedom and risk at the same time. If you lose your seed phrase, nobody can reset it. If you keep coins on an exchange, you do not fully own them. See <a href="/blog/how-to-store-bitcoin-safely.html">how to store Bitcoin safely</a>.</p>
<h2>What Bitcoin is not</h2>
<p>Bitcoin is not a guaranteed investment. Price moves a lot. Bitcoin is also not “all of crypto.” Most tokens are different assets with different rules. Start with <a href="/blog/bitcoin-vs-crypto.html">Bitcoin vs crypto</a> before you buy anything else.</p>
<h2>A sane first path</h2>
<p>Learn the words. Get a wallet you control. Buy a small amount you can afford to lose. Practice sending a tiny test. Back up your seed phrase on paper, offline. Then ignore noise. <a href="/start.html">The full path is here</a>.</p>
"""

BODIES["how-to-buy-bitcoin"] = """
<p>Buying Bitcoin is easy. Keeping it is the part beginners skip. This guide covers a first purchase and the handoff to a wallet you control.</p>
<h2>Before you buy</h2>
<ul>
<li>Only use money you can afford to lose.</li>
<li>Write down the difference between an exchange account and a wallet you control.</li>
<li>Have a plan for <a href="/blog/bitcoin-wallet-for-beginners.html">where the coins will live</a> after you buy.</li>
</ul>
<h2>Step 1: Choose a regulated on-ramp</h2>
<p>In the US and many other countries, you buy Bitcoin through an exchange or broker that verifies identity (KYC). Look for a well-known company, two-factor authentication, and withdrawals that actually work. This article does not recommend a specific brand because those change.</p>
<h2>Step 2: Create the account and turn on 2FA</h2>
<p>Use a password manager. Turn on app-based two-factor authentication, not SMS if you can avoid it. Phishing sites copy exchange logins. Type the URL yourself. Never enter your seed phrase on an exchange. Exchanges do not need it.</p>
<h2>Step 3: Fund and place a small buy</h2>
<p>Link a bank transfer or debit method. Buy a small amount first. Market orders fill immediately at the current price. Limit orders wait for a price you set. Fees vary. Read them before you click.</p>
<h2>Step 4: Withdraw to your wallet</h2>
<p>Copy your Bitcoin receive address from your wallet. Send a tiny test first. Confirm it arrived. Then send the rest. This is how you leave “IOU Bitcoin” on an exchange and hold actual Bitcoin. Full detail: <a href="/blog/how-to-store-bitcoin-safely.html">self-custody</a>.</p>
<h2>Common beginner mistakes</h2>
<ul>
<li>Leaving everything on the exchange forever.</li>
<li>Buying because a stranger on social media promised returns.</li>
<li>Sending to the wrong network (Bitcoin is not Ethereum).</li>
<li>No test transaction.</li>
</ul>
<p>If you want a calmer buying habit after the first purchase, read <a href="/blog/dollar-cost-averaging-bitcoin.html">dollar-cost averaging</a>.</p>
"""

BODIES["bitcoin-wallet-for-beginners"] = """
<p>A Bitcoin wallet does not store coins like a leather billfold. The coins live on the blockchain. The wallet stores keys that prove you can spend them.</p>
<h2>Hot vs cold</h2>
<p><strong>Hot wallets</strong> live on a phone or computer connected to the internet. They are convenient for small amounts. <strong>Cold wallets</strong> (often hardware devices) keep keys offline. They are better for savings you do not spend daily.</p>
<h2>The seed phrase</h2>
<p>When you create a wallet, you get 12 or 24 words. That seed phrase is the backup. Anyone who has it can take the Bitcoin. Anyone who loses it, with no other backup, loses the Bitcoin. Write it on paper. Do not screenshot it. Do not email it. Do not store it in iCloud.</p>
<h2>Addresses</h2>
<p>Your wallet can generate many receive addresses. Sharing an address is normal. Sharing a seed phrase is never normal. Double-check the first and last characters when you paste an address. Malware can swap clipboard addresses.</p>
<h2>Exchange accounts are not wallets</h2>
<p>If the company holds the keys, you have a balance in their database. That can be useful for buying. It is not self-custody. Move savings out. See <a href="/blog/how-to-store-bitcoin-safely.html">safe storage</a> and <a href="/blog/how-to-buy-bitcoin.html">how to buy</a>.</p>
"""

BODIES["how-to-store-bitcoin-safely"] = """
<p>Self-custody means you hold the keys. That is the point of Bitcoin. It also means you cannot call support if you mess up.</p>
<h2>A practical setup</h2>
<ol>
<li>Use a reputable hardware wallet for amounts that would hurt to lose.</li>
<li>Initialize it yourself. Do not buy a “pre-set up” device from a random seller.</li>
<li>Write the seed phrase on paper or steel. Store it offline. Consider two locations.</li>
<li>Do a recovery test with a tiny amount before you deposit savings.</li>
<li>Send a test receive and a test spend.</li>
</ol>
<h2>What not to do</h2>
<ul>
<li>Do not type your seed into a website that “validates” it.</li>
<li>Do not take photos of the words.</li>
<li>Do not tell people how much you hold.</li>
<li>Do not keep life-changing sums on a phone wallet.</li>
</ul>
<p>Learn wallet types in <a href="/blog/bitcoin-wallet-for-beginners.html">the wallet guide</a>. If you are still buying on an exchange, plan the withdrawal in <a href="/blog/how-to-buy-bitcoin.html">how to buy Bitcoin</a>.</p>
<h2>Inheritance</h2>
<p>If nobody can find the seed, the coins are gone when you are. A simple written instruction, a lawyer, or a multi-person plan matters more than people admit. This is not legal advice. It is a reminder that Bitcoin does not come with a customer-service reset.</p>
"""

BODIES["bitcoin-vs-crypto"] = """
<p>People say “crypto” the way they say “the market.” It hides differences that matter. Bitcoin is one network with one monetary policy. Crypto is a marketing bucket for thousands of tokens.</p>
<h2>Bitcoin</h2>
<p>Fixed supply. Hard to change the base rules. No CEO. No equity token. The asset is the money of the network. Security comes from proof-of-work and a huge miner + node set. Start with <a href="/blog/what-is-bitcoin.html">what Bitcoin is</a>.</p>
<h2>Everything else</h2>
<p>Many coins have foundations, venture investors, and the ability to mint more units. Some are experiments. Some are casinos. Some are copies. A beginner who buys “crypto” as a category is usually buying a grab bag of risk they cannot name.</p>
<h2>Why this site is Bitcoin-only</h2>
<p>You can learn one thing well. Wallets, fees, self-custody, and scams are already enough. After you can buy, withdraw, and back up Bitcoin, you will be harder to fool. That is the skill. Not picking 40 tickers.</p>
"""

BODIES["how-bitcoin-mining-works"] = """
<p>Mining is how Bitcoin adds new blocks and how new coins enter circulation. It is not a beginner way to “get free Bitcoin” on a laptop.</p>
<h2>What miners do</h2>
<p>Miners collect transactions, race to find a valid proof-of-work hash, and publish a block. The winner gets the block subsidy plus fees. The subsidy halves about every four years. That is the halving. Total issuance still heads toward 21 million.</p>
<h2>Why energy?</h2>
<p>Proof-of-work makes rewriting history expensive. You cannot vote the ledger into a fake past without outrunning the honest chain. Energy is the cost of that defense. Whether that energy mix is “good” is a separate debate. The mechanism is not optional if you want Bitcoin’s security model.</p>
<h2>You can use Bitcoin without mining</h2>
<p>Users need wallets and verification, not ASICs. If you want the money, read <a href="/blog/how-to-buy-bitcoin.html">how to buy</a> and <a href="/blog/how-to-store-bitcoin-safely.html">how to store it</a>. Mining is infrastructure, not a starter side hustle.</p>
"""

BODIES["dollar-cost-averaging-bitcoin"] = """
<p>Dollar-cost averaging (DCA) means buying a fixed dollar amount on a schedule — weekly or monthly — instead of trying to pick the perfect day.</p>
<h2>Why beginners like it</h2>
<p>Bitcoin’s price is noisy. DCA removes the fantasy of a perfect entry. You still buy an asset that can fall a lot. DCA is a behavior, not a guarantee of profit.</p>
<h2>How to do it without getting sloppy</h2>
<ul>
<li>Pick an amount that does not change your rent payment.</li>
<li>Automate the buy if your on-ramp allows it.</li>
<li>Withdraw to self-custody on a cadence you will actually follow.</li>
<li>Do not DCA with borrowed money.</li>
</ul>
<p>Buying is only half. Combine this with <a href="/blog/how-to-buy-bitcoin.html">the buy guide</a> and <a href="/blog/how-to-store-bitcoin-safely.html">storage</a>.</p>
"""

BODIES["bitcoin-glossary"] = """
<p>Learn these words first. Then the rest of Bitcoin content gets easier.</p>
<h2>Core terms</h2>
<p><strong>Address.</strong> Where you receive Bitcoin. Shareable. Not secret like a seed.</p>
<p><strong>Block.</strong> A batch of transactions added to the chain.</p>
<p><strong>Blockchain.</strong> The public history of Bitcoin transactions.</p>
<p><strong>Cold storage.</strong> Keys kept offline.</p>
<p><strong>Confirmation.</strong> A transaction sitting in a mined block. More blocks on top = harder to reverse.</p>
<p><strong>Exchange.</strong> A company where you buy and sell. They often hold keys for you until you withdraw.</p>
<p><strong>Fee.</strong> Paid to miners to get into a block. Higher fees usually confirm faster.</p>
<p><strong>Halving.</strong> The cut in new-coin issuance about every four years.</p>
<p><strong>Hardware wallet.</strong> A device that keeps keys offline and signs transactions.</p>
<p><strong>Hot wallet.</strong> Software wallet on a connected phone or computer.</p>
<p><strong>HODL.</strong> Slang for holding long term. Not a strategy by itself.</p>
<p><strong>Keys.</strong> Secret data that proves you can spend coins.</p>
<p><strong>Lightning.</strong> A layer for faster, cheaper payments on top of Bitcoin.</p>
<p><strong>Mempool.</strong> Waiting room for unconfirmed transactions.</p>
<p><strong>Miner.</strong> A participant who produces blocks using proof-of-work.</p>
<p><strong>Node.</strong> Software that verifies the rules and the chain.</p>
<p><strong>Private key.</strong> Secret. Lets you spend. Never share.</p>
<p><strong>Public key / address.</strong> Derived from keys. Safe to share as a receive address.</p>
<p><strong>Sats (satoshis).</strong> The small unit of Bitcoin. 100,000,000 sats = 1 BTC.</p>
<p><strong>Seed phrase.</strong> The human-readable backup of a wallet. Guard it.</p>
<p><strong>Self-custody.</strong> You hold the keys.</p>
<p><strong>UTXO.</strong> An unspent output. Bitcoin’s way of tracking amounts you can spend.</p>
<p>Use the glossary with <a href="/start.html">the start-here path</a>.</p>
"""


def article_schema(p):
    return f"""<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{p['title']}","datePublished":"{p['date']}","dateModified":"{p['date']}","author":{{"@type":"Organization","name":"Learn Bitcoin Fast"}},"publisher":{{"@type":"Organization","name":"Learn Bitcoin Fast"}},"mainEntityOfPage":"{SITE}/blog/{p['slug']}.html","description":"{p['desc']}"}}</script>"""


for p in POSTS:
    related = [x for x in POSTS if x["slug"] != p["slug"]][:3]
    rel_html = "".join(
        f'<a class="card block" href="/blog/{x["slug"]}.html"><h3>{x["h1"]}</h3></a>'
        for x in related
    )
    body = f"""
  <main class="wrap" style="padding:3rem 0">
    <article class="prose">
      <p class="kicker">Guide · {p["read"]} · Updated {p["date"]}</p>
      <h1>{p["h1"]}</h1>
      <p class="lede">{p["desc"]}</p>
      {BODIES[p["slug"]]}
      <p class="fine">Educational content only. Not financial advice.</p>
    </article>
    <section style="margin-top:2rem">
      <h2>Keep learning</h2>
      <div class="grid-3">{rel_html}</div>
    </section>
  </main>
"""
    write(
        f'blog/{p["slug"]}.html',
        page(
            f'{p["title"]} | Learn Bitcoin Fast',
            p["desc"],
            f'/blog/{p["slug"]}.html',
            body,
            "/blog/",
            "article",
            extra=f'<meta name="keywords" content="{p["kw"]}">\n  {article_schema(p)}',
        ),
    )

chapter_html = []
for i, (slug, label) in enumerate(chapters):
    chapter_html.append(
        f'<article class="chapter" data-page="{i}" hidden>'
        f'<p class="book-meta">{label} · {i+1} / {len(chapters)}</p>'
        f'<h1>{label.split("·",1)[-1].strip()}</h1>'
        f'{BODIES[slug]}'
        f'</article>'
    )
read_body = f"""
  <main class="wrap">
    <div class="reader">
      <button class="page-btn" id="prev" type="button" aria-label="Previous page">←</button>
      <div class="book-page prose" id="page">
        {''.join(chapter_html)}
      </div>
      <button class="page-btn" id="next" type="button" aria-label="Next page">→</button>
    </div>
    <p class="fine" style="text-align:center">Use the arrows or your keyboard left/right keys to turn pages. <a href="/book/">Back to the book</a></p>
  </main>
  <script>
    (function () {{
      var pages = [].slice.call(document.querySelectorAll('.chapter'));
      var i = 0;
      function show(n) {{
        i = Math.max(0, Math.min(pages.length - 1, n));
        pages.forEach(function (p, idx) {{ p.hidden = idx !== i; }});
        document.getElementById('prev').disabled = i === 0;
        document.getElementById('next').disabled = i === pages.length - 1;
        window.scrollTo({{ top: 0, behavior: 'smooth' }});
      }}
      document.getElementById('prev').onclick = function () {{ show(i - 1); }};
      document.getElementById('next').onclick = function () {{ show(i + 1); }};
      document.addEventListener('keydown', function (e) {{
        if (e.key === 'ArrowLeft') show(i - 1);
        if (e.key === 'ArrowRight') show(i + 1);
      }});
      show(0);
    }})();
  </script>
"""
write("book/read/index.html", page(
    "Read Bitcoin Blueprint | Learn Bitcoin Fast",
    "Read the Bitcoin Blueprint online with page-turn navigation: eight beginner chapters from what Bitcoin is to self-custody.",
    "/book/read/",
    read_body,
    "/book/",
))

write(
    "404.html",
    page(
        "Page not found | Learn Bitcoin Fast",
        "That page is missing. Go back to Learn Bitcoin Fast.",
        "/404.html",
        '<main class="wrap" style="padding:4rem 0"><h1>Page not found</h1><p><a href="/">Home</a> · <a href="/blog/">Blog</a></p></main>',
    ),
)

urls = ["/", "/start.html", "/about.html", "/contact.html", "/privacy.html", "/blog/", "/book/", "/book/read/"]
urls += [f"/blog/{p['slug']}.html" for p in POSTS]
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in urls:
    sm.append(f"  <url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod></url>")
sm.append("</urlset>")
(ROOT / "sitemap.xml").write_text("\n".join(sm), encoding="utf-8")

(ROOT / "robots.txt").write_text(
    f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n",
    encoding="utf-8",
)

(ROOT / ".htaccess").write_text(
    """RewriteEngine On
RewriteCond %{HTTPS} off [OR]
RewriteCond %{HTTP_HOST} !^www\\.learnbitcoinfast\\.com$ [NC]
RewriteRule ^ https://www.learnbitcoinfast.com%{REQUEST_URI} [L,R=301]
ErrorDocument 404 /404.html
<IfModule mod_headers.c>
  Header always set Strict-Transport-Security "max-age=31536000"
</IfModule>
""",
    encoding="utf-8",
)

(ROOT / "README-UPLOAD.txt").write_text(
    """LEARN BITCOIN FAST — upload to Hostinger public_html

1. Open Hostinger File Manager for learnbitcoinfast.com
2. Open public_html
3. Upload everything in this folder (index.html, start.html, about.html, blog, css, robots.txt, sitemap.xml, .htaccess)
4. Keep folder structure: css/ and blog/ stay as folders

This site is static HTML. No database.

After upload, request indexing in Google Search Console for https://www.learnbitcoinfast.com/sitemap.xml
""",
    encoding="utf-8",
)

print("done")
