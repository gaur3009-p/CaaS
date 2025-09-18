import gradio as gr
from agents.linda_agent.ad_copy_generator import AdCopyGenerator
from agents.linda_agent.image_generator import ImageGenerator
from agents.mike_agent.sentiment_analyzer import SentimentAnalyzer
from agents.glue_agent.workflow_orchestrator import WorkflowOrchestrator

def generate_creatives(brand_guidelines: str):
    ad_copy_generator = AdCopyGenerator()
    ad_copy = ad_copy_generator.generate_ad_copy(brand_guidelines)

    image_generator = ImageGenerator()
    image_path = image_generator.generate_image(brand_guidelines)

    sentiment_analyzer = SentimentAnalyzer()
    feedback_score = sentiment_analyzer.analyze_feedback("User feedback: Great ad!", ad_copy)

    return ad_copy, image_path, f"Feedback Score: {feedback_score:.2f}"

with gr.Blocks() as demo:
    gr.Markdown("# AI-Powered Creative Campaign Generator")
    with gr.Row():
        brand_input = gr.Textbox(label="Brand Guidelines", placeholder="Describe your brand and campaign goals...")
        submit_btn = gr.Button("Generate Creatives")
    with gr.Row():
        ad_copy_output = gr.Textbox(label="Generated Ad Copy")
        image_output = gr.Image(label="Generated Ad Image")
        feedback_output = gr.Textbox(label="Feedback Score")

    submit_btn.click(
        fn=generate_creatives,
        inputs=brand_input,
        outputs=[ad_copy_output, image_output, feedback_output]
    )

demo.launch()
