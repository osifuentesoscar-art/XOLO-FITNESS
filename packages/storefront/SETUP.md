# Storefront setup

`index.html` is a single, self-contained static page — no build step, no
backend. It can be deployed as-is to any static host (or dropped into
xolofit.com's site builder as a custom page).

## Before this can take payments

The three "Subscribe" buttons in the Pricing section are placeholders —
search `index.html` for `<!-- SETUP:` to find all three. Each needs a real
[Stripe Payment Link](https://dashboard.stripe.com/payment-links):

1. In the Stripe dashboard, create a recurring monthly product for each
   tier: **Self-Guided ($75/mo)**, **XOLOKAN-Personalized ($150/mo)**,
   **Premium / Hybrid ($200/mo)** — pricing confirmed in
   `docs/business/XOLOKAN_PRODUCT_SYSTEM.md`.
2. Create a Payment Link for each product.
3. Replace the matching `href="#"` in `index.html` with that Payment
   Link's URL. No other code changes needed — Payment Links handle
   checkout, subscription billing, and receipts without a custom backend.

## What's not built yet

- No account/login system — a subscriber's access to the personalized tier
  (the XOLOKAN chat app in `packages/web`) isn't yet connected to their
  Stripe subscription. That wiring (webhook -> access grant) is the next
  real engineering step once payments are live.
- No individual product pages — this is a single landing page. Splitting
  each protocol into its own page is straightforward if wanted later.
