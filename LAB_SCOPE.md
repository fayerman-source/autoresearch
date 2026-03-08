# Lab Scope

This repository is a separate research sandbox forked from `karpathy/autoresearch`.

It is intentionally **not** part of:
- `adhara-private`
- `shanta-yantra`

## Purpose

Use this lab to learn whether autonomous keep/discard experiment loops are useful for our own work.

The immediate questions are:
- can the stronger desktop run this workflow comfortably?
- what parts of the protocol are worth borrowing?
- does the agent actually produce useful iterative progress?
- which ideas transfer to a future Shanta-specific research harness?

## Non-Purpose

This repo is not the Shanta product.
It is not the Adhara architecture.
It is not a place to mix contemplative product code with unrelated model-training experiments.

## Working Boundary

Keep this repo focused on:
- upstream `autoresearch` experimentation
- hardware validation
- loop design
- adaptation ideas

Bring ideas back to Shanta only after they are proven useful.

## Initial Plan

1. Verify the Acer Nitro environment.
2. Run the upstream setup with minimal changes.
3. Measure VRAM, runtime, and stability.
4. Decide whether to:
   - keep using this fork for generic loop research
   - or build a fresh Shanta-specific research repo inspired by the protocol

## Success Condition

This lab is successful if it gives us a clear answer about whether autonomous research loops are worth adapting for Shanta.
