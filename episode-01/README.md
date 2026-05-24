# Episode 1 — Welcome + Foundation Setup

Welcome to the **Building an E-commerce Contact Center with Amazon Connect**
series. This is Episode 1 — the foundation episode. By the end of this video
you'll have everything in place to start building the contact center over the
next 12 episodes.

📺 **Watch the video:** [link to YouTube]
📂 **Full playlist:** [link to playlist]

## What you'll build in this episode

A complete Amazon Connect foundation for ShopEasy, our fictional online
retailer. You'll set up:

- Hours of operation
- Three queues (General Support, Returns, Callbacks)
- A custom security profile
- Two routing profiles (Tier 1 and Tier 2 agents)
- Agent users
- Your first login to the Contact Control Panel

By the end, you'll be able to call your toll-free number and have it ring
in your agent workspace.

## Before you start

You'll need:

- An AWS account (free tier works)
- An existing Amazon Connect instance — if you don't have one yet, watch
  [my Amazon Connect instance setup video] first
- A claimed phone number on your instance (toll-free recommended for US)

## The resources you'll create

Use these exact names so the rest of the series matches what you build:

| Resource | Name |
|---|---|
| Hours of Operation | ShopEasy Business Hours |
| Queue | General Support |
| Queue | Returns |
| Queue | Callbacks |
| Security Profile | ShopEasy Agent |
| Routing Profile | Tier 1 Agent |
| Routing Profile | Tier 2 Agent |

## Hours of operation

- Monday – Friday: 9:00 AM – 9:00 PM EST
- Saturday – Sunday: 10:00 AM – 6:00 PM EST

## Routing profile setup

**Tier 1 Agent**
- Queues: General Support (priority 1), Returns (priority 2)
- Channel concurrency: voice = 1, chat = 2
- Default outbound queue: General Support

**Tier 2 Agent**
- Queues: General Support (priority 2), Returns (priority 1), Callbacks (priority 1)
- Channel concurrency: voice = 1, chat = 2
- Default outbound queue: Returns

## Quick troubleshooting

**My toll-free number doesn't ring my CCP.**
Make sure your agent user is assigned to a routing profile, the routing profile
has at least one queue, and you're set to "Available" status in the CCP.

**I can't find the "Routing profiles" menu.**
You need the Admin security profile (or a custom one with Users & Permissions
access). Log in as the admin user from your instance setup.

**Hours of operation profile won't save.**
Double-check the timezone field — it's required and easy to miss on first pass.

## What's coming next

**Episode 2 — Inbound IVR with Four-Option Menu.** We build the actual call
flow: greeting, business hours check, four-option menu, queue routing.
Everything you set up in this episode gets used.

## Get the most out of this series

- ⭐ Star the [GitHub repo] to follow along
- 🔔 Subscribe and turn on notifications
- 💬 Drop questions in the comments — I read all of them
- 🎯 Follow the full [playlist] from start to finish

---

Built as part of the ShopEasy Amazon Connect series. Questions? comment on the video.
