# LTX-Video Generator Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                    LTX-Video Generator                       │
│                  Text-to-Video Generation                    │
└─────────────────────────────────────────────────────────────┘

┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   User Input │    │   LTX-Video  │    │   Output     │
│              │    │     Model    │    │   Video      │
│  Text Prompt │───▶│              │───▶│              │
│              │    │  (LTX 2.3)   │    │  .mp4 file   │
│  Settings    │    │              │    │              │
│  - Frames    │    │  Diffusion   │    │  Download    │
│  - Steps     │    │  Pipeline    │    │  Ready!      │
│  - Guidance  │    │              │    │              │
│  - Seed      │    │  GPU         │    │              │
│  - FPS       │    │  Accelerated │    │              │
└──────────────┘    └──────────────┘    └──────────────┘
       │                   │                   │
       │                   │                   │
       ▼                   ▼                   ▼
  ┌─────────┐        ┌─────────┐        ┌─────────┐
  │ Gradio  │        │  Hugging│        │  Local  │
  │   UI    │        │  Face   │        │  File   │
  │  Simple │        │  Hub    │        │  System │
  │  One-   │        │  Model  │        │         │
  │  Click  │        │  Download│        │         │
  └─────────┘        └─────────┘        └─────────┘

┌─────────────────────────────────────────────────────────────┐
│                      Quick Start                              │
│                                                              │
│  1. Open in Google Colab (GPU Runtime)                       │
│  2. Run all cells                                            │
│  3. Enter your text prompt                                    │
│  4. Click "Generate Video"                                   │
│  5. Download your video!                                     │
│                                                              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                    Example Prompts                           │
│                                                              │
│  🌸 "A serene Japanese garden with cherry blossoms..."      │
│  🚀 "An astronaut floating in space with Earth..."          │
│  🌲 "A magical forest with glowing mushrooms..."             │
│  🌊 "Ocean waves crashing on a rocky beach..."               │
│  🤖 "A cute robot exploring a colorful alien planet..."     │
│                                                              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                    Performance                               │
│                                                              │
│  GPU        │ VRAM  │ Time (49 frames)                      │
│  ─────────────────────────────────────────────────────────  │
│  T4         │ 16GB  │ ~2-3 minutes                          │
│  V100       │ 32GB  │ ~1-2 minutes                          │
│  A100       │ 40GB  │ ~30-60 seconds                        │
│                                                              │
└─────────────────────────────────────────────────────────────┘

Made with ❤️ by Vikram Bosak
GitHub: https://github.com/Vikram-Bosak/ltx-video-generator
