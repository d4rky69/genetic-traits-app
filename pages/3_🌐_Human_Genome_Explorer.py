import streamlit as st
import random
from utils.pdf_export import add_pdf_export, load_css

st.set_page_config(page_title="Human Genome Explorer", page_icon="🌐", layout="wide")
load_css()

st.title("🔬 Human Genome Project Interactive Portal")
st.markdown("An educational and interactive website to explore the Human Genome Project, genetic traits, mutations, and chromosome maps.")

tabs = st.tabs([
    "🏠 Homepage",
    "🧬 Trait Analyzer",
    "🧪 Mutation Simulator",
    "🗺️ Chromosome Map",
    "ℹ️ About"
])

# --- Tab 1: Homepage ---
with tabs[0]:
    st.header("What is the Human Genome Project?")
    st.markdown("""
    The **Human Genome Project (HGP)** was an international scientific effort from **1990 to 2003** to map all 3 billion DNA base pairs in humans.  
    Its completion revolutionized medicine, genetics, ancestry research, and disease studies.

    **Key Outcomes:**
    - Entire human DNA sequence mapped.
    - Identified 20,000+ genes.
    - Enabled new treatments for genetic disorders.
    - Advanced personalized medicine and ancestry science.

    **Why is it important?**
    - Helps us understand how genes shape traits, health, and diversity.
    - Supports research into genetic diseases.
    - Lays the foundation for modern genetics, gene therapy, and precision healthcare.
    """)

# --- Tab 2: Trait Analyzer ---
with tabs[1]:
    st.header("🧬 Trait Analyzer: Dominant vs Recessive")
    st.markdown("Select a trait to learn if it is **dominant or recessive**, and which gene controls it.")
    trait_db = {
        "Eye Color": {
            "Brown": {"type": "Dominant", "gene": "OCA2", "chromosome": 15, "explanation": "Brown eyes are dominant. The OCA2 gene on chromosome 15 controls melanin production in the iris."},
            "Blue": {"type": "Recessive", "gene": "OCA2 (variant)", "chromosome": 15, "explanation": "Blue eyes are recessive. They result from a variant in the OCA2 gene decreasing melanin in the iris."}
        },
        "Blood Type": {
            "Type A": {"type": "Dominant", "gene": "ABO", "chromosome": 9, "explanation": "A blood type is dominant over O. The ABO gene on chromosome 9 determines blood group."},
            "Type O": {"type": "Recessive", "gene": "ABO", "chromosome": 9, "explanation": "O blood type is recessive. Both copies must be O alleles."},
            "Type B": {"type": "Dominant", "gene": "ABO", "chromosome": 9, "explanation": "B blood type is dominant over O. The ABO gene determines this."}
        },
        "Lactose Tolerance": {
            "Tolerant": {"type": "Dominant", "gene": "LCT", "chromosome": 2, "explanation": "Lactose tolerance is dominant. Controlled by LCT gene on chromosome 2."},
            "Intolerant": {"type": "Recessive", "gene": "LCT", "chromosome": 2, "explanation": "Lactose intolerance is recessive. Both copies must have the variant."}
        },
        "Dimples": {
            "Yes": {"type": "Dominant", "gene": "Unknown", "chromosome": "-", "explanation": "Dimples are usually dominant, but the gene is not fully characterized."},
            "No": {"type": "Recessive", "gene": "Unknown", "chromosome": "-", "explanation": "No dimples is recessive."}
        }
    }
    trait = st.selectbox("Choose a trait", list(trait_db.keys()))
    value = st.selectbox("Select trait value", list(trait_db[trait].keys()))
    info = trait_db[trait][value]
    st.markdown(f"""
        **Trait:** {trait}  
        **Value:** {value}  
        **Inheritance:** `{info['type']}`  
        **Gene:** `{info['gene']}`  
        **Chromosome:** `{info['chromosome']}`  
        **Explanation:** {info['explanation']}
    """)

# --- Tab 3: Mutation Simulator ---
with tabs[2]:
    st.header("🧪 Mutation Simulator")
    st.markdown("Enter a short DNA sequence (e.g., `ATCGGA`). The simulator will apply a random mutation.")
    dna_input = st.text_input("DNA Sequence (A, T, C, G only)", "")
    mutation_result = ""
    if st.button("Simulate Mutation"):
        def mutate(seq):
            if not seq or any(c not in "ATCG" for c in seq.upper()):
                return ("Invalid sequence. Only letters A, T, C, G allowed.", None)
            seq = seq.upper()
            mutation_type = random.choice(["insertion", "deletion", "substitution"])
            pos = random.randint(0, len(seq)-1) if seq else 0
            if mutation_type == "insertion":
                base = random.choice("ATCG")
                mutated_seq = seq[:pos] + base + seq[pos:]
                explanation = f"Insertion of {base} at position {pos+1}"
            elif mutation_type == "deletion" and len(seq) > 1:
                mutated_seq = seq[:pos] + seq[pos+1:]
                explanation = f"Deletion at position {pos+1}"
            else:  # substitution
                base = random.choice([b for b in "ATCG" if b != seq[pos]])
                mutated_seq = seq[:pos] + base + seq[pos+1:]
                explanation = f"Substitution of {seq[pos]}→{base} at position {pos+1}"
            return (mutated_seq, explanation)
        mutated, explanation = mutate(dna_input)
        if mutated and explanation:
            st.markdown(f"**Original DNA:** `{dna_input}`")
            st.markdown(f"**Mutation Type:** {explanation}")
            st.markdown(f"**Mutated DNA:** `{mutated}`")
            # Example: sickle cell mutation
            if "deletion" in explanation or "substitution" in explanation:
                st.info("Example: A substitution mutation in the **HBB** gene (chromosome 11) can cause Sickle Cell Anemia by changing one amino acid in hemoglobin.")
        else:
            st.error(mutated)

# --- Tab 4: Chromosome Map ---
with tabs[3]:
    st.header("🗺️ Chromosome Map (Simplified)")
    st.markdown("Click a chromosome to see example genes and their functions.")
    chromo_map = {
        "Chromosome 11": [
            {"gene": "HBB", "function": "Hemoglobin beta (Sickle cell anemia)"},
            {"gene": "INS", "function": "Insulin (blood sugar regulation)"}
        ],
        "Chromosome 15": [
            {"gene": "OCA2", "function": "Eye color"},
            {"gene": "FBN1", "function": "Connective tissue (Marfan syndrome)"}
        ],
        "Chromosome 19": [
            {"gene": "APOE", "function": "Alzheimer’s risk"},
            {"gene": "LDLR", "function": "Cholesterol metabolism"}
        ],
        "Chromosome X": [
            {"gene": "DMD", "function": "Dystrophin (muscular dystrophy)"},
            {"gene": "FMR1", "function": "Fragile X syndrome"}
        ]
    }
    chromo = st.selectbox("Select Chromosome", list(chromo_map.keys()))
    st.markdown(f"### Genes on {chromo}:")
    for g in chromo_map[chromo]:
        st.markdown(f"- **{g['gene']}**: {g['function']}")

# --- Tab 5: About Page ---
with tabs[4]:
    st.header("ℹ️ About the Human Genome Project")
    st.markdown("""
    **Timeline:**  
    - 1990: Project launched.  
    - 1995: Bacterial genome sequenced.  
    - 2000: First draft of human genome completed.  
    - 2003: Final human genome published.

    **Collaborators:**  
    - USA, UK, Japan, France, Germany, China, and more.  
    - Organizations: NIH, Wellcome Trust, DOE, universities worldwide.

    **Applications:**  
    - Personalized medicine
    - Ancestry testing
    - Disease research

    **Ethical Considerations:**  
    - Privacy of genetic data
    - Genetic discrimination

    **Educational Goal:**  
    To make genetics approachable and fun, demonstrating how the HGP unlocked new knowledge about DNA, traits, and health.
    """)
    add_pdf_export()
