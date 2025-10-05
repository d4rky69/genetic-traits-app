import streamlit as st
import random
import numpy as np
from utils.pdf_export import add_pdf_export, load_css

st.set_page_config(page_title="Human Genome Explorer", page_icon="🌐", layout="wide")
load_css()

# --- Back to Home button ---
if st.button("🏠 Back to Home", key="back_home_genome", use_container_width=True):
    st.session_state["project_choice"] = None
    st.switch_page("Home.py")

st.title("🔬 Human Genome Project Interactive Portal")
st.markdown("An educational and interactive website to explore the Human Genome Project, genetic traits, mutations, and chromosome maps.")

tabs = st.tabs([
    "🏠 Homepage",
    "🧬 Trait Analyzer",
    "🧪 Mutation Simulator",
    "🗺️ Chromosome Map (Basic)",
    "🗺️ Chromosome Map (Advanced)",
    "🧬 Genetic Algorithm Explorer",
    "🧩 Genome Assembly Challenge",
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
    st.info("Tip: If tabs overflow, scroll right →", icon="➡️")

# --- Tab 2: Trait Analyzer ---
with tabs[1]:
    st.header("🧬 Trait Analyzer: Dominant vs Recessive")
    st.markdown("Select a trait to learn if it is **dominant or recessive**, and which gene controls it.")
    trait_db = {
        "Eye Color": {
            "Brown": {"type": "Dominant", "gene": "OCA2", "chromosome": 15, "explanation": "Brown eyes are dominant. The OCA2 gene on chromosome 15 controls melanin production in the iris."},
            "Blue": {"type": "Recessive", "gene": "OCA2 (variant)", "chromosome": 15, "explanation": "Blue eyes are recessive. They result from a variant in the OCA2 gene decreasing melanin in the iris."},
            "Black": {"type": "Dominant", "gene": "OCA2", "chromosome": 15, "explanation": "Black eyes are dominant. OCA2 gene controls this pigment."}
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
            if "deletion" in explanation or "substitution" in explanation:
                st.info("Example: A substitution mutation in the **HBB** gene (chromosome 11) can cause Sickle Cell Anemia by changing one amino acid in hemoglobin.")
        else:
            st.error(mutated)

# --- Tab 4: Chromosome Map (Basic) ---
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

# --- Tab 5: Chromosome Map (Advanced) ---
with tabs[4]:
    st.header("🗺️ Simplified Chromosome Map")
    st.markdown("An interactive map of selected human chromosomes. Select a chromosome to discover key genes and their functions.")

    advanced_chromosomes = {
        "Chromosome 1 (~2,000 Genes)": {
            "summary": "Largest human chromosome. Contains many important genes related to development and disease.",
            "genes": [
                {"name": "MTHFR", "desc": "Methylenetetrahydrofolate reductase (folate metabolism)", "locus": "1p36.22"},
                {"name": "F5", "desc": "Coagulation factor V (blood clotting)", "locus": "1q23"}
            ]
        },
        "Chromosome 4 (~750 Genes)": {
            "summary": "Contains genes involved in skeletal development and immunity.",
            "genes": [
                {"name": "FGFR3", "desc": "Fibroblast growth factor receptor 3 (bone growth)", "locus": "4p16.3"}
            ]
        },
        "Chromosome 6 (~1,000 Genes)": {
            "summary": "Important for immune system function (HLA region).",
            "genes": [
                {"name": "HLA-A", "desc": "Major histocompatibility complex, class I, A", "locus": "6p21.3"}
            ]
        },
        "Chromosome 7 (~1,150 Genes)": {
            "summary": "One of the 23 pairs of chromosomes in humans. It spans about 159 million base pairs and represents over 5% of the total DNA in cells.",
            "genes": [
                {"name": "CFTR", "desc": "Provides instructions for making a protein called the cystic fibrosis transmembrane conductance regulator. Mutations in this gene cause Cystic Fibrosis.", "locus": "7q31.2"},
                {"name": "EGFR", "desc": "Epidermal growth factor receptor, a gene that can turn into an oncogene when mutated, and is associated with multiple cancers.", "locus": "7p12"}
            ]
        },
        "Chromosome 11 (~1,300 Genes)": {
            "summary": "Contains genes involved in hemoglobin and insulin production.",
            "genes": [
                {"name": "HBB", "desc": "Hemoglobin beta (Sickle cell anemia)", "locus": "11p15.4"},
                {"name": "INS", "desc": "Insulin (blood sugar regulation)", "locus": "11p15.5"}
            ]
        },
        "Chromosome 12 (~1,050 Genes)": {
            "summary": "Genes related to metabolism and immunity.",
            "genes": [
                {"name": "VDR", "desc": "Vitamin D receptor", "locus": "12q13.11"}
            ]
        },
        "Chromosome 15 (~600 Genes)": {
            "summary": "Genes controlling eye color, connective tissue.",
            "genes": [
                {"name": "OCA2", "desc": "Eye color", "locus": "15q12"},
                {"name": "FBN1", "desc": "Connective tissue (Marfan syndrome)", "locus": "15q21.1"}
            ]
        },
        "Chromosome 17 (~1,200 Genes)": {
            "summary": "Genes related to cancer and neurological disorders.",
            "genes": [
                {"name": "TP53", "desc": "Tumor protein p53", "locus": "17p13.1"}
            ]
        },
        "Chromosome 19 (~1,500 Genes)": {
            "summary": "Genes involved in cholesterol metabolism and Alzheimer’s risk.",
            "genes": [
                {"name": "APOE", "desc": "Alzheimer’s risk", "locus": "19q13.32"},
                {"name": "LDLR", "desc": "Cholesterol metabolism", "locus": "19p13.2"}
            ]
        },
        "Chromosome 21 (~200-300 Genes)": {
            "summary": "Smallest autosome, contains genes related to Down syndrome.",
            "genes": [
                {"name": "APP", "desc": "Amyloid precursor protein", "locus": "21q21.3"}
            ]
        },
        "Chromosome 22 (~500 Genes)": {
            "summary": "Genes linked to immune system and growth.",
            "genes": [
                {"name": "COMT", "desc": "Catechol-O-methyltransferase (dopamine metabolism)", "locus": "22q11.21"}
            ]
        }
    }

    chromo_choice = st.selectbox("Select Chromosome", list(advanced_chromosomes.keys()))
    chromo_info = advanced_chromosomes[chromo_choice]
    st.markdown(f'''
        <div class="chromosome-info-box">
            <b>{chromo_choice.split("(")[0].strip()}</b>
            <div class="chromosome-desc">{chromo_info['summary']}</div>
        </div>
    ''', unsafe_allow_html=True)

    st.subheader("Notable Genes:")
    for gene in chromo_info["genes"]:
        st.markdown(f'''
            <div class="gene-card">
                <b>{gene["name"]}</b>
                <span class="gene-locus">{gene["locus"]}</span>
                <div class="gene-desc">{gene["desc"]}</div>
            </div>
        ''', unsafe_allow_html=True)

# --- Tab 6: Genetic Algorithm Explorer ---
with tabs[5]:
    st.header("🧬 Genetic Algorithm Explorer")
    st.markdown("Simulate natural selection by setting parameters and evolving a population of DNA sequences towards a target.")

    def fitness(seq, target):
        return sum(a == b for a, b in zip(seq, target)) / len(target)

    def evolve(target, pop_size, mutation_rate, max_gens):
        population = [''.join(random.choices('ATCG', k=len(target))) for _ in range(pop_size)]
        best_seq = ""
        best_fit = 0
        generations = 0
        for g in range(max_gens):
            fitnesses = [fitness(seq, target) for seq in population]
            best_idx = np.argmax(fitnesses)
            if fitnesses[best_idx] > best_fit:
                best_fit = fitnesses[best_idx]
                best_seq = population[best_idx]
            if best_fit == 1.0:
                generations = g + 1
                break
            selected = random.choices(population, weights=fitnesses, k=pop_size)
            new_pop = []
            for i in range(pop_size):
                parent = selected[random.randint(0, pop_size-1)]
                child = list(parent)
                for j in range(len(child)):
                    if random.random() < mutation_rate:
                        child[j] = random.choice('ATCG')
                new_pop.append(''.join(child))
            population = new_pop
        else:
            generations = max_gens
        return best_seq, best_fit, generations

    with st.form("ga_form"):
        target_seq = st.text_input("Target DNA Sequence (A, T, C, G)", value="ATGC")
        pop_size = st.slider("Population Size", min_value=10, max_value=200, value=100)
        mutation_rate = st.slider("Mutation Rate", min_value=0.001, max_value=0.1, value=0.01, step=0.001)
        max_gens = st.slider("Max Generations", min_value=10, max_value=500, value=100)
        submitted = st.form_submit_button("Run Simulation", type="primary")
    if submitted:
        with st.spinner("Running genetic algorithm..."):
            best_seq, best_fit, gens = evolve(target_seq, pop_size, mutation_rate, max_gens)
            st.success(f"Simulation Complete. Evolved over {gens} generations.")
            st.markdown("### Simulation Results")
            st.progress(best_fit)
            st.metric("Best Fitness Achieved", f"{best_fit*100:.2f}%")
            st.markdown(f"**Target Sequence:** `{target_seq}`")
            st.markdown(f"**Best Evolved Sequence:** `{best_seq}`")
            if best_fit == 1.0:
                st.info("Target sequence perfectly matched!", icon="✅")
            else:
                st.warning("Target sequence not fully matched.", icon="⚠️")

# --- Tab 7: Genome Assembly Challenge ---
with tabs[6]:
    st.header("🧩 Genome Assembly Challenge")
    st.markdown("Reconstruct the original DNA sequence by correctly ordering the overlapping fragments below.")

    full_sequence = "CGATTATGCGGTAC"
    fragments = ["CGATT", "ATGCG", "CGGTAC", "TATGCG"]

    if "assembly_order" not in st.session_state:
        st.session_state["assembly_order"] = []

    if "assembly_available" not in st.session_state:
        st.session_state["assembly_available"] = fragments.copy()

    def reset_assembly():
        st.session_state["assembly_order"] = []
        st.session_state["assembly_available"] = fragments.copy()

    def get_overlap(a, b):
        max_olap = 0
        for i in range(1, min(len(a), len(b))):
            if a[-i:] == b[:i]:
                max_olap = i
        return max_olap

    def assemble_fragments(order):
        if not order:
            return ""
        result = order[0]
        for frag in order[1:]:
            olap = get_overlap(result, frag)
            result += frag[olap:]
        return result

    st.button("Reset / Shuffle", on_click=reset_assembly)
    st.markdown("#### Your Assembled Sequence")
    assembled = assemble_fragments(st.session_state["assembly_order"])
    st.code(assembled if assembled else "No fragments selected.")

    st.markdown("#### Available Fragments (Click to add in order)")

    options = ["Select a fragment..."] + st.session_state["assembly_available"]
    if len(options) > 1:
        fragment_clicked = st.radio(
            "Select a fragment to add",
            options,
            key="frag_radio",
            index=0,
            label_visibility="collapsed"
        )
        if fragment_clicked != "Select a fragment...":
            st.session_state["assembly_order"].append(fragment_clicked)
            st.session_state["assembly_available"].remove(fragment_clicked)
            st.session_state["frag_radio"] = "Select a fragment..."
            st.experimental_rerun()

    if st.button("Check Assembly"):
        if assembled == full_sequence:
            st.success("Correct! Sequence assembled.")
        else:
            st.error("Incorrect assembly. Try again or use Reset.")

    if st.button("Hint"):
        for frag in fragments:
            if full_sequence.startswith(frag):
                st.info(f"Try starting with: {frag}")
                break

# --- Tab 8: About Page ---
with tabs[7]:
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
