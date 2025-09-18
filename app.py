import gradio as gr
from agents.linda import LindaAgent
from agents.mike import MikeAgent
from agents.glue import GlueAgent
from agents.persona import PersonaAgent
from agents.deployment import DeploymentAgent
from agents.compliance import ComplianceAgent

linda = LindaAgent()
mike = MikeAgent()
glue = GlueAgent()
persona = PersonaAgent()
deployment = DeploymentAgent()
compliance = ComplianceAgent()

def generate_campaign(brand_guideline, audience, tone):
    brand_tone = persona.extract_brand_tone(brand_guideline)
    audience_info = persona.extract_audience(audience)

    ad_copy = linda.generate_ad_copy(brand_guideline)
    ad_scripts = linda.generate_ad_script(f"Write an ad script for {audience} with {tone} tone")
    poster = linda.generate_poster(f"Poster for {brand_guideline} targeting {audience}")

    creatives = [
        {
            "ad_copy": ad_copy[0]["summary_text"],
            "ad_script": script["generated_text"],
            "poster": poster,
            "score": 0.75
        }
        for script in ad_scripts
    ]

    ranked = mike.rank_creatives(creatives)
    best = ranked[0]

    if not compliance.check_compliance(best["ad_copy"]):
        return "Compliance check failed.", "", None

    return best["ad_copy"], best["ad_script"], best["poster"]

with gr.Blocks() as demo:
    gr.Markdown("# AI Campaign Agent")
    with gr.Row():
        brand = gr.Textbox(label="Brand Guideline", placeholder="Describe your brand and campaign goals...")
        audience = gr.Textbox(label="Target Audience", placeholder="Who is your target audience?")
        tone = gr.Textbox(label="Tone", placeholder="What tone should the campaign have?")
    submit = gr.Button("Generate Campaign")
    with gr.Row():
        ad_copy = gr.Textbox(label="Ad Copy", interactive=False)
        ad_script = gr.Textbox(label="Ad Script", interactive=False)
        poster = gr.Image(label="Poster", interactive=False)
    submit.click(
        fn=generate_campaign,
        inputs=[brand, audience, tone],
        outputs=[ad_copy, ad_script, poster]
    )

demo.launch()
