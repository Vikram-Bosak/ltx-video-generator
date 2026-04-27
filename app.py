#!/usr/bin/env python3
"""
LTX-Video Text-to-Video Generator
Simple script to generate videos from text prompts
"""

import torch
from diffusers import LTXVideoPipeline
from diffusers.utils import export_to_video
import gradio as gr
import numpy as np
import os
from datetime import datetime

# Check GPU
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"🎯 Using device: {device}")
if device == "cuda":
    print(f"📊 GPU: {torch.cuda.get_device_name(0)}")
    print(f"💾 VRAM: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB")

# Load model
print("📥 Loading LTX-Video model...")
print("⏳ This may take 2-3 minutes on first run...")

pipe = LTXVideoPipeline.from_pretrained(
    "Lightricks/LTX-Video",
    torch_dtype=torch.float16,
    variant="fp16"
).to(device)

# Enable memory optimizations
pipe.enable_model_cpu_offload()
pipe.enable_xformers_memory_efficient_attention()

print("✅ Model loaded successfully!")

def generate_video(
    prompt,
    negative_prompt="",
    num_frames=49,
    num_inference_steps=20,
    guidance_scale=2.5,
    seed=-1,
    fps=24
):
    """
    Generate video from text prompt using LTX-Video
    """
    print(f"🎬 Generating video for: {prompt}")
    print(f"⚙️ Settings: {num_frames} frames, {num_inference_steps} steps, guidance={guidance_scale}")

    # Set seed for reproducibility
    if seed != -1:
        torch.manual_seed(seed)
        np.random.seed(seed)

    # Generate video
    with torch.no_grad():
        video = pipe(
            prompt=prompt,
            negative_prompt=negative_prompt,
            num_frames=num_frames,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale,
            generator=torch.Generator(device).manual_seed(seed) if seed != -1 else None
        ).frames[0]

    # Save video
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"ltx_video_{timestamp}.mp4"

    export_to_video(video, output_path, fps=fps)

    print(f"✅ Video saved to: {output_path}")
    print(f"📊 Video size: {os.path.getsize(output_path) / (1024*1024):.1f} MB")

    return output_path

# Create Gradio interface
with gr.Blocks(title="LTX-Video Generator", theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 🎬 LTX-Video Text-to-Video Generator
    
    Generate amazing videos from text descriptions using LTX-Video (LTX 2.3) model!
    
    ---
    """)

    with gr.Row():
        with gr.Column():
            # Text prompt input
            prompt_input = gr.Textbox(
                label="✍️ Your Prompt",
                placeholder="Describe the video you want to create...",
                lines=3,
                value="A cinematic shot of a futuristic city at sunset, with flying cars and neon lights reflecting on glass buildings"
            )

            # Negative prompt
            negative_prompt = gr.Textbox(
                label="🚫 Negative Prompt (optional)",
                placeholder="Things to avoid in the video...",
                lines=2,
                value="blurry, low quality, distorted, ugly, bad anatomy"
            )

            # Advanced settings (collapsed)
            with gr.Accordion("⚙️ Advanced Settings", open=False):
                num_frames = gr.Slider(
                    minimum=9,
                    maximum=121,
                    value=49,
                    step=2,
                    label="🎞️ Number of Frames"
                )

                num_steps = gr.Slider(
                    minimum=10,
                    maximum=50,
                    value=20,
                    step=1,
                    label="🔄 Inference Steps"
                )

                guidance_scale = gr.Slider(
                    minimum=1.0,
                    maximum=10.0,
                    value=2.5,
                    step=0.1,
                    label="🎯 Guidance Scale"
                )

                seed = gr.Number(
                    value=-1,
                    label="🎲 Seed (-1 for random)"
                )

                fps = gr.Slider(
                    minimum=8,
                    maximum=60,
                    value=24,
                    step=1,
                    label="📹 FPS"
                )

            # Generate button
            generate_btn = gr.Button(
                "🎬 Generate Video",
                variant="primary",
                size="lg"
            )

        with gr.Column():
            # Output video
            video_output = gr.Video(
                label="🎥 Generated Video",
                autoplay=True,
                show_label=True
            )

            # Status message
            status = gr.Textbox(
                label="📊 Status",
                value="Ready to generate!",
                interactive=False
            )

    # Example prompts
    gr.Examples(
        examples=[
            ["A serene Japanese garden with cherry blossoms falling gently, koi fish swimming in a crystal clear pond", "blurry, low quality"],
            ["An astronaut floating in space with Earth in the background, cinematic lighting", "distorted, ugly"],
            ["A magical forest with glowing mushrooms and fireflies at night, fantasy style", "bad anatomy"],
            ["Ocean waves crashing on a rocky beach during golden hour, slow motion", "blurry"],
            ["A cute robot exploring a colorful alien planet, animated style", "low quality"]
        ],
        inputs=[prompt_input, negative_prompt],
        label="💡 Example Prompts"
    )

    # Define button click handler
    def on_generate(prompt, neg_prompt, frames, steps, guidance, seed_val, fps_val):
        if not prompt.strip():
            return None, "❌ Please enter a prompt!"

        status_msg = f"🎬 Generating video...\nPrompt: {prompt[:50]}..."
        yield None, status_msg

        try:
            video_path = generate_video(
                prompt=prompt,
                negative_prompt=neg_prompt,
                num_frames=int(frames),
                num_inference_steps=int(steps),
                guidance_scale=float(guidance),
                seed=int(seed_val),
                fps=int(fps_val)
            )
            return video_path, f"✅ Video generated successfully!\n📁 Saved as: {os.path.basename(video_path)}"
        except Exception as e:
            return None, f"❌ Error: {str(e)}"

    # Connect button to function
    generate_btn.click(
        fn=on_generate,
        inputs=[prompt_input, negative_prompt, num_frames, num_steps, guidance_scale, seed, fps],
        outputs=[video_output, status]
    )

print("✅ UI created successfully!")
print("🚀 Launching LTX-Video Generator...")
print("📱 Click the link below to open the interface!")

demo.launch(
    share=True,  # Creates a public link
    debug=False,
    show_error=True
)
