# Comprehensive Agronomic Crop Disease Advisory Database
# Maps timm/ttr classification tags directly to expert advisory profiles

ADVISORY_DATABASE = {
    # ── TOMATO DISEASES ──────────────────────────────────────────────────────
    "Tomato___Bacterial_spot": {
        "crop": "Tomato",
        "disease_name": "Bacterial Spot",
        "cause": "Xanthomonas bacteria (primarily Xanthomonas perforans)",
        "description": "A destructive bacterial disease that affects leaves, stems, and fruit, causing significant yield losses in warm, wet conditions.",
        "symptoms": [
            "Small, water-soaked, circular spots on leaves that turn dark brown or black.",
            "Leaf spots may merge, causing leaves to yellow, wither, and drop prematurely.",
            "Small, raised, scab-like black spots on green and ripe tomato fruit."
        ],
        "organic_control": [
            "Apply copper-based organic bactericides early in the growing season.",
            "Use compost tea or Bacillus subtilis formulations to strengthen foliage immune defenses.",
            "Prune lower foliage to prevent soil splashback and increase airflow."
        ],
        "chemical_control": [
            "Spray copper hydroxide (e.g., Kocide) combined with Mancozeb if weather conditions are persistently wet.",
            "Utilize Agri-Mycin (streptomycin) during early vegetative stages (not close to harvest)."
        ],
        "prevention": [
            "Use certified pathogen-free seeds and disease-resistant tomato varieties.",
            "Avoid overhead irrigation; use drip or soaker hoses to keep leaves dry.",
            "Rotate crops with non-solanaceous plants for at least 2-3 years."
        ],
        "severity_level": "Medium"
    },
    "Tomato___Early_blight": {
        "crop": "Tomato",
        "disease_name": "Early Blight",
        "cause": "Alternaria solani (fungus)",
        "description": "One of the most common tomato diseases, characterized by distinctive target-shaped dark brown spots starting on older lower foliage.",
        "symptoms": [
            "Dark spots on older leaves with concentric rings resembling a bullseye target.",
            "Leaves yellow around the target spots and drop, exposing developing tomatoes to sunscald.",
            "Dark, sunken, leathery lesions near the stem end of the fruit."
        ],
        "organic_control": [
            "Mulch heavily around the base of plants with straw or plastic to block soil spores.",
            "Spray copper-based organic fungicides or Serenade ASO (Bacillus amyloliquefaciens) weekly.",
            "Thoroughly prune and destroy infected lower foliage immediately."
        ],
        "chemical_control": [
            "Apply chlorothalonil (e.g., Daconil) or mancozeb at the first sign of symptoms.",
            "Use systemic fungicides containing azoxystrobin (e.g., Quadris) for severe outbreaks."
        ],
        "prevention": [
            "Maintain generous 3-foot spacing between tomato plants for optimal air circulation.",
            "Avoid working in the garden when tomato plants are wet with dew or rain.",
            "Thoroughly clean up and discard crop residues at the end of the season."
        ],
        "severity_level": "Medium"
    },
    "Tomato___Late_blight": {
        "crop": "Tomato",
        "disease_name": "Late Blight",
        "cause": "Phytophthora infestans (oomycete/water mold)",
        "description": "An extremely aggressive, highly infectious disease that can destroy entire tomato fields in days under cool, humid weather.",
        "symptoms": [
            "Large, dark, water-soaked brown lesions on leaves and stems.",
            "A delicate white, fuzzy mold growth on the undersides of leaves during wet weather.",
            "Large, firm, greasy golden-brown leathery spots on tomato fruit."
        ],
        "organic_control": [
            "Apply copper octanoate or copper soap preventative sprays early and often.",
            "There is no organic cure once late blight is fully established; immediately pull and burn plants."
        ],
        "chemical_control": [
            "Apply active preventative fungicides such as chlorothalonil, mancozeb, or copper.",
            "Use specialized oomycete targeted chemicals like Orondis, Ranman, or Revus Top for commercial fields."
        ],
        "prevention": [
            "Plant only certified disease-resistant varieties (e.g., Mountain Merit, Defiant).",
            "Eliminate volunteer tomato plants and solanaceous weeds (nightshade) near the field.",
            "Monitor regional agricultural extension alerts for active late blight outbreaks."
        ],
        "severity_level": "Severe"
    },
    "Tomato___Leaf_Mold": {
        "crop": "Tomato",
        "disease_name": "Leaf Mold",
        "cause": "Passalora fulva (fungus)",
        "description": "Commonly occurs in high-humidity greenhouse environments, leading to leaf yellowing and severe defoliation.",
        "symptoms": [
            "Pale green or yellow spots on the upper leaf surface.",
            "Olive-green to gray, velvety fungal growth on the matching undersides of leaves.",
            "Affected leaves curl, dry up, and drop off in severe infections."
        ],
        "organic_control": [
            "Dramatically reduce relative humidity in greenhouses (keep below 85%).",
            "Apply organic biofungicides like Bacillus subtilis or potassium bicarbonate solutions."
        ],
        "chemical_control": [
            "Spray preventive fungicides such as chlorothalonil or copper fungicides.",
            "Utilize strobilurin class fungicides if severe greenhouse infections spread."
        ],
        "prevention": [
            "Use exhaust fans, open side vents, and prune tomatoes to optimize indoor airflow.",
            "Select resistant greenhouse varieties."
        ],
        "severity_level": "Low"
    },
    "Tomato___Septoria_leaf_spot": {
        "crop": "Tomato",
        "disease_name": "Septoria Leaf Spot",
        "cause": "Septoria lycopersici (fungus)",
        "description": "A foliage-destroying disease that starts on lower leaves and quickly spreads upwards, leading to sunscald on tomatoes.",
        "symptoms": [
            "Numerous small, circular spots with dark brown margins and light gray centers.",
            "Tiny black specks (pycnidia spores) visible in the center of mature leaf spots.",
            "Leaves turn yellow, dry up, and fall off rapidly."
        ],
        "organic_control": [
            "Apply copper-based organic fungicides at 7 to 10-day intervals.",
            "Heavily mulch with clean organic material to prevent soil-borne spores from splashing up."
        ],
        "chemical_control": [
            "Spray chlorothalonil, mancozeb, or copper fungicides at the first sign of lower leaf spotting."
        ],
        "prevention": [
            "Rotate crops out of tomatoes, potatoes, and peppers for 3 years.",
            "Prune off and safely destroy the lowest 24 inches of branches."
        ],
        "severity_level": "Medium"
    },
    "Tomato___Spider_mites_Two-spotted_spider_mite": {
        "crop": "Tomato",
        "disease_name": "Two-Spotted Spider Mites",
        "cause": "Tetranychus urticae (pest/arachnid)",
        "description": "Tiny sap-sucking pests that thrive in hot, dry weather, causing foliage speckling and webbing.",
        "symptoms": [
            "Fine white or yellow speckling (stippling) on the upper surface of leaves.",
            "Silky, fine webbing on the undersides of leaves and around stems.",
            "Leaves turn bronze, dry up, and fall off under high pest populations."
        ],
        "organic_control": [
            "Release predatory mites (Phytoseiulus persimilis) to feed on the spider mites.",
            "Spray plants thoroughly with neem oil, horticultural oils, or insecticidal soaps."
        ],
        "chemical_control": [
            "Apply specialized miticides/acaricides (e.g., Abamectin, Spiromesifen) on the foliage undersides."
        ],
        "prevention": [
            "Keep tomato plants well-watered to prevent dry soil conditions that attract mites.",
            "Periodically spray plants with high-pressure water hoses to knock down mite colonies."
        ],
        "severity_level": "Low"
    },
    "Tomato___Target_Spot": {
        "crop": "Tomato",
        "disease_name": "Target Spot",
        "cause": "Corynespora cassiicola (fungus)",
        "description": "Causes circular spots with target-like rings on leaves and dark sunken lesions on tomatoes.",
        "symptoms": [
            "Circular leaf spots with pale centers and dark rings.",
            "Large, dark, sunken circular spots on tomato fruit that expand as fruit matures."
        ],
        "organic_control": [
            "Apply biofungicides containing Bacillus amyloliquefaciens.",
            "Clean and sterilize all tomato cages and staking equipment."
        ],
        "chemical_control": [
            "Apply DMI or QoI fungicides (e.g., Azoxystrobin, Pyraclostrobin) periodically."
        ],
        "prevention": [
            "Avoid planting near old crops of tomatoes, cucumbers, or cotton.",
            "Utilize wide plant spacing and keep leaves dry."
        ],
        "severity_level": "Medium"
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "crop": "Tomato",
        "disease_name": "Tomato Yellow Leaf Curl Virus (TYLCV)",
        "cause": "Geminivirus (transmitted by Silverleaf Whitefly)",
        "description": "A devastating viral disease that severely stunts plants and prevents fruit set, spread entirely by whiteflies.",
        "symptoms": [
            "New leaves are extremely small, curled upward, and yellowed along margins.",
            "Severe stunting of the plant, giving it a bushy, compact appearance.",
            "Flower drop occurs, resulting in little to no fruit development."
        ],
        "organic_control": [
            "Control whitefly vectors using yellow sticky cards and insecticidal soaps.",
            "Spray neem oil or pyrethrins to reduce whitefly feeding activity."
        ],
        "chemical_control": [
            "Use systemic insecticides (e.g., Imidacloprid, Acetamiprid) to control whitefly vector colonies."
        ],
        "prevention": [
            "Grow TYLCV-resistant tomato varieties (e.g., Sunchaser, Tycoon).",
            "Cover young seedlings with fine floating row covers to exclude whitefly insects."
        ],
        "severity_level": "Severe"
    },
    "Tomato___Tomato_mosaic_virus": {
        "crop": "Tomato",
        "disease_name": "Tomato Mosaic Virus (ToMV)",
        "cause": "Tobamovirus",
        "description": "A highly stable, extremely infectious virus spread mechanically by contact and contaminated tools.",
        "symptoms": [
            "Mottled green and yellow mosaic patterns on leaves.",
            "Leaves may be distorted, narrow, or resemble fern leaves ('shoestring' symptom).",
            "Internal browning and uneven ripening of tomato fruit."
        ],
        "organic_control": [
            "There is no chemical or organic cure for virus-infected plants; remove and burn them immediately.",
            "Soak pruning tools in a 20% dry milk solution or trisodium phosphate between plants."
        ],
        "chemical_control": [
            "None. Viricides are not commercially available for agricultural plant crops."
        ],
        "prevention": [
            "Wash hands with soap and water after handling tobacco products (can carry related viruses).",
            "Plant only certified virus-free seeds and resistant tomato cultivars."
        ],
        "severity_level": "Severe"
    },

    # ── POTATO DISEASES ──────────────────────────────────────────────────────
    "Potato___Early_blight": {
        "crop": "Potato",
        "disease_name": "Early Blight",
        "cause": "Alternaria solani (fungus)",
        "description": "Affects both foliage and tubers, causing characteristic target-like brown spots on leaves and corky dry rot in stored potatoes.",
        "symptoms": [
            "Dark brown circular spots on older leaves with concentric ring patterns.",
            "Leaf tissue between spots yellows, dies, and drops.",
            "Sunken, dark, dry, leathery decay spots on potato tubers."
        ],
        "organic_control": [
            "Apply copper fungicides or biofungicides containing Bacillus amyloliquefaciens.",
            "Maintain optimal soil nitrogen levels (stressed plants are more susceptible)."
        ],
        "chemical_control": [
            "Spray preventative chlorothalonil or mancozeb at regular intervals during wet, warm weather."
        ],
        "prevention": [
            "Use certified disease-free seed potatoes.",
            "Rotate crops out of potatoes, eggplants, and tomatoes for 3 years.",
            "Harvest only after vines are fully dead to prevent tuber infection."
        ],
        "severity_level": "Medium"
    },
    "Potato___Late_blight": {
        "crop": "Potato",
        "disease_name": "Late Blight",
        "cause": "Phytophthora infestans (oomycete)",
        "description": "The disease responsible for the historic Irish Potato Famine; causes rapid leaf death and completely rots tubers in the ground or in storage.",
        "symptoms": [
            "Large, irregular, water-soaked dark green to black spots on leaves.",
            "Fuzzy white fungal growth on the underside of leaves during damp conditions.",
            "Tubers show a dark brown, dry, granular rot extending into the flesh."
        ],
        "organic_control": [
            "Apply copper-based organic fungicides preventatively.",
            "Destroy all volunteer potatoes and cull piles near fields."
        ],
        "chemical_control": [
            "Use robust oomycete-targeted protectants and systemic chemicals (e.g., Fluopicolide, Cyazofamid)."
        ],
        "prevention": [
            "Avoid overhead irrigation entirely; ensure optimal soil drainage.",
            "Kill vines chemically or mechanically 2 weeks before harvest to protect tubers."
        ],
        "severity_level": "Severe"
    },

    # ── APPLE DISEASES ───────────────────────────────────────────────────────
    "Apple___Apple_scab": {
        "crop": "Apple",
        "disease_name": "Apple Scab",
        "cause": "Venturia inaequalis (fungus)",
        "description": "A serious fungal disease that damages leaves and developing fruit, causing unsightly brown scab lesions.",
        "symptoms": [
            "Olive-green, velvety, circular spots on leaves that turn dark brown to black.",
            "Raised, corky, dark brown scabby lesions on apple skins.",
            "Affected apples become misshapen, crack open, and drop prematurely."
        ],
        "organic_control": [
            "Apply organic sulfur sprays or liquid copper at green tip and petal fall stages.",
            "Spray lime-sulfur early in the spring before blossoms open."
        ],
        "chemical_control": [
            "Use preventative fungicides (e.g., Captan, Myclobutanil) starting at bud break."
        ],
        "prevention": [
            "Rake, chop, and compost or bury fallen leaves in autumn to eliminate overwintering spores.",
            "Plant scab-resistant cultivars (e.g., Liberty, Enterprise, Freedom)."
        ],
        "severity_level": "Medium"
    },
    "Apple___Black_rot": {
        "crop": "Apple",
        "disease_name": "Black Rot / Frogeye Leaf Spot",
        "cause": "Botryosphaeria obtusa (fungus)",
        "description": "Causes cankers on tree limbs, frogeye leaf spots, and complete rot of apples starting at the blossom end.",
        "symptoms": [
            "Leaf spots with a purple border and light brown center ('frogeye' appearance).",
            "Apple rot starts as a dark brown spot at the blossom end and forms dark concentric rings.",
            "Sunken, dark, cracked cankers on bark of branches and twigs."
        ],
        "organic_control": [
            "Prune out dead wood, cankers, and mummified apples during winter dormancy.",
            "Spray copper fungicides during early spring before leaves expand fully."
        ],
        "chemical_control": [
            "Apply fungicides containing captan or thiophanate-methyl starting at bud break."
        ],
        "prevention": [
            "Burn or dispose of all pruned wood (canker spores overwinter in dead branches).",
            "Ensure trees are pruned to allow plenty of sunlight into the inner canopy."
        ],
        "severity_level": "Medium"
    },
    "Apple___Cedar_apple_rust": {
        "crop": "Apple",
        "disease_name": "Cedar Apple Rust",
        "cause": "Gymnosporangium juniperi-virginianae (fungus)",
        "description": "A dual-host fungus that cycles between apple trees and eastern red cedars, causing glowing bright orange leaf spots.",
        "symptoms": [
            "Bright yellow-orange, circular spots on the upper leaf surface in early summer.",
            "Tiny tube-like projections (aecia) on the underside of infected leaves.",
            "Orange, gelatinous, horn-like galls on nearby cedar trees during spring rains."
        ],
        "organic_control": [
            "Apply liquid copper or sulfur sprays at the first sign of orange spots.",
            "Remove nearby eastern red cedar trees (within 1/2 mile) if possible."
        ],
        "chemical_control": [
            "Spray systemic fungicides like myclobutanil (e.g., Immunox) at pink bud stage."
        ],
        "prevention": [
            "Plant rust-resistant apple varieties (e.g., Red Delicious, Empire).",
            "Apply protectant sprays when nearby cedar galls become orange and jelly-like."
        ],
        "severity_level": "Medium"
    },

    # ── CORN DISEASES ────────────────────────────────────────────────────────
    "Corn___Cercospora_leaf_spot_Gray_leaf_spot": {
        "crop": "Corn",
        "disease_name": "Gray Leaf Spot",
        "cause": "Cercospora zeae-maydis (fungus)",
        "description": "A serious foliar disease in warm, humid regions that blocks photosynthesis, leading to stalk breakage and poor grain fill.",
        "symptoms": [
            "Small tan spots on leaves that turn into long, narrow, rectangular gray spots.",
            "Spots are strictly bordered by leaf veins, creating sharp, blocky borders.",
            "Entire leaves turn brown, die, and shred during warm wet weather."
        ],
        "organic_control": [
            "Incorporate old corn crop residues into the soil to accelerate decomposition.",
            "Rotate crops out of corn for at least 2 seasons."
        ],
        "chemical_control": [
            "Apply foliar fungicides (e.g., Strobilurins, Triazoles) at tassel emergence (V12 to VT stages)."
        ],
        "prevention": [
            "Select high-yielding corn hybrids with genetic resistance to Gray Leaf Spot.",
            "Implement conventional tillage to bury overwintered spore-bearing residues."
        ],
        "severity_level": "Medium"
    },
    "Corn___Common_rust": {
        "crop": "Corn",
        "disease_name": "Common Rust",
        "cause": "Puccinia sorghi (fungus)",
        "description": "Characterized by powdery, reddish-brown pustules on leaves, commonly spreading in cool, moist climates.",
        "symptoms": [
            "Raised, powdery, cinnamon-brown spots (pustules) on both upper and lower leaf surfaces.",
            "Pustules rupture, releasing millions of rusty-orange spores.",
            "Severe cases cause yellowing, leaf death, and reduced kernel quality."
        ],
        "organic_control": [
            "Remove and destroy infected garden corn stalks immediately.",
            "Apply sulfur-based organic dusts or copper sprays early in the infection."
        ],
        "chemical_control": [
            "Commercial fields rarely need chemical control; if needed, apply triazole fungicides."
        ],
        "prevention": [
            "Plant rust-resistant corn hybrids.",
            "Avoid late planting dates, as younger plants are more susceptible to airborne rust spores."
        ],
        "severity_level": "Low"
    },
    "Corn___Northern_Leaf_Blight": {
        "crop": "Corn",
        "disease_name": "Northern Corn Leaf Blight",
        "cause": "Exserohilum turcicum (fungus)",
        "description": "An aggressive fungal disease that causes large, cigar-shaped leaf lesions, threatening feed and grain yields.",
        "symptoms": [
            "Long, narrow, grayish-green to tan spots that resemble a cigar (up to 6 inches long).",
            "Spots have rounded ends and are not bordered strictly by leaf veins.",
            "Dark, dusty olive-green fungal spores visible inside the lesions during wet weather."
        ],
        "organic_control": [
            "Apply preventative biofungicides containing Bacillus strains.",
            "Till crop residues deep into the soil after harvest."
        ],
        "chemical_control": [
            "Use triazole and strobilurin combination fungicides before canopy closure."
        ],
        "prevention": [
            "Rotate out of corn for at least 1-2 years.",
            "Select resistant corn hybrids (look for Ht-genes in crop sheets)."
        ],
        "severity_level": "Medium"
    },

    # ── GRAPE DISEASES ───────────────────────────────────────────────────────
    "Grape___Black_rot": {
        "crop": "Grape",
        "disease_name": "Black Rot",
        "cause": "Guignardia bidwellii (fungus)",
        "description": "One of the most damaging grape diseases globally; turns fresh grapes into shriveled, hard black mummies.",
        "symptoms": [
            "Small circular tan spots on leaves with a distinct dark brown border.",
            "Grapes turn pale, soften, and quickly shrivel into wrinkled black mummies.",
            "Tiny black dots (fruiting bodies) cover the surface of rotted grapes."
        ],
        "organic_control": [
            "Hand-pick and remove all mummified grapes from vines and soil during pruning.",
            "Apply organic copper-based fungicides starting at bud break."
        ],
        "chemical_control": [
            "Spray highly effective systemic fungicides (e.g., Mancozeb, Myclobutanil) from pre-bloom to post-bloom."
        ],
        "prevention": [
            "Keep vines trellised high and prune dense canopies to maximize sunlight and airflow.",
            "Maintain clean ground cover beneath grapevines to prevent splash spores."
        ],
        "severity_level": "Severe"
    },
    "Grape___Esca_(Black_Measles)": {
        "crop": "Grape",
        "disease_name": "Esca / Black Measles",
        "cause": "Phacidiopycnis/Phaeoacremonium (complex wood fungi)",
        "description": "A complex vascular disease affecting mature grapevines, causing dramatic tiger-stripe patterns on leaves and small dark spots on grapes.",
        "symptoms": [
            "Leaves show striking yellow and dark brown 'tiger-stripe' necrosis between veins.",
            "Grapes show small, dark, round spots resembling measles.",
            "Wood shows dark cracks, decay, and black vascular streaks inside the vine trunk."
        ],
        "organic_control": [
            "Avoid mechanical damage to trunks; apply organic pruning wound sealants.",
            "Remove and replace severely diseased vines showing sudden collapse (apoplexy)."
        ],
        "chemical_control": [
            "No direct chemical cure exists; protect pruning wounds with fungicides like thiophanate-methyl."
        ],
        "prevention": [
            "Avoid pruning vines during wet weather when wood-rotting fungal spores are flying.",
            "Use only certified clean nursery grapevine cuttings."
        ],
        "severity_level": "Medium"
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "crop": "Grape",
        "disease_name": "Isariopsis Leaf Blight",
        "cause": "Pseudocercospora vitis (fungus)",
        "description": "Foliar disease that causes premature leaf fall in late summer, affecting grapevine vigor and winter hardiness.",
        "symptoms": [
            "Irregular, dull brown spots on older leaves that expand dynamically.",
            "Undersides of leaf spots show a dusty dark brown coating of fungal spores.",
            "Severely spotted leaves curl, dry, and drop off ahead of autumn."
        ],
        "organic_control": [
            "Spray copper or sulfur fungicides to protect mature foliage.",
            "Gather and destroy fallen leaves in winter to prevent spring reinfections."
        ],
        "chemical_control": [
            "Apply standard broad-spectrum vineyard fungicides as part of regular spray schedules."
        ],
        "prevention": [
            "Optimize canopy microclimates through selective leaf pulling near fruit zones.",
            "Maintain balanced fertilization."
        ],
        "severity_level": "Low"
    },

    # ── SQUASH & CUCURBIT DISEASES ───────────────────────────────────────────
    "Squash___Powdery_mildew": {
        "crop": "Squash",
        "disease_name": "Powdery Mildew",
        "cause": "Podosphaera xanthii (fungus)",
        "description": "Forms a dusty white coating over leaves, severely reducing squash yields and causing leaves to die in hot climates.",
        "symptoms": [
            "White, powdery spots that expand to cover entire leaves and stems.",
            "Leaves look as if they were dusted with talcum powder.",
            "Infected leaves turn yellow, brown, and dry up, leaving squash exposed to sunscald."
        ],
        "organic_control": [
            "Spray potassium bicarbonate or baking soda mixed with horticultural oil.",
            "Apply organic neem oil or sulfur dusts weekly."
        ],
        "chemical_control": [
            "Spray systemic fungicides like myclobutanil or triadimefon if infection is widespread."
        ],
        "prevention": [
            "Provide ample spacing between vines to encourage rapid drying of foliage.",
            "Grow squash in full sun locations with excellent drainage."
        ],
        "severity_level": "Medium"
    },

    # ── STRAWBERRY DISEASES ──────────────────────────────────────────────────
    "Strawberry___Leaf_scorch": {
        "crop": "Strawberry",
        "disease_name": "Leaf Scorch",
        "cause": "Diplocarpon earlianum (fungus)",
        "description": "A common foliage disease that forms large purplish blotches, making strawberry leaves appear scorched and dried.",
        "symptoms": [
            "Numerous dark purple spots on leaves that expand to form large, irregular purplish-brown blotches.",
            "Leaves dry up and curl at the margins, resembling sun or wind scorch.",
            "Stems of fruit can also be girdled, causing small, sour strawberries."
        ],
        "organic_control": [
            "Prune off older spotted leaves during spring garden maintenance.",
            "Apply copper fungicides during early vegetative growth."
        ],
        "chemical_control": [
            "Use protectant fungicides (e.g., Captan, Pyraclostrobin) before fruit set."
        ],
        "prevention": [
            "Renovate strawberry beds after harvest by mowing leaves and removing old runners.",
            "Keep beds weed-free to maximize air circulation."
        ],
        "severity_level": "Low"
    },

    # ── ORANGE & CITRUS DISEASES ─────────────────────────────────────────────
    "Orange___Haunglongbing_(Citrus_greening)": {
        "crop": "Orange",
        "disease_name": "Citrus Greening (Huanglongbing - HLB)",
        "cause": "Candidatus Liberibacter bacteria (vectored by Asian Citrus Psyllid)",
        "description": "The most destructive citrus disease in the world. Clogs the tree's vascular system, causing bitter, lopsided green fruit and killing trees.",
        "symptoms": [
            "Asymmetrical yellow mottling on leaves ('blotchy mottle' pattern).",
            "Citrus fruit is small, lopsided, has a bitter taste, and remains green at the bottom.",
            "Severe leaf drop, twig dieback, and gradual death of the citrus tree."
        ],
        "organic_control": [
            "Strictly control the Asian Citrus Psyllid vectors using yellow sticky traps and horticultural oils.",
            "Pull out and burn infected citrus trees immediately to protect neighboring orchards."
        ],
        "chemical_control": [
            "None available for the bacteria. Treat orchards with insecticides (e.g., Neonicotinoids) to suppress vector psyllids."
        ],
        "prevention": [
            "Plant only certified disease-free citrus stock from screened nurseries.",
            "Apply reflective mulches in young groves to repel psyllid vectors."
        ],
        "severity_level": "Severe"
    },

    # ── PEACH & STONE FRUIT DISEASES ─────────────────────────────────────────
    "Peach___Bacterial_spot": {
        "crop": "Peach",
        "disease_name": "Bacterial Spot",
        "cause": "Xanthomonas arboricola pv. pruni (bacteria)",
        "description": "Affects peach leaves, twigs, and fruit, causing severe leaf drop and deep cracking in developing peaches.",
        "symptoms": [
            "Small pale green to yellow leaf spots that turn brown and fall out, leaving a 'shot-hole' appearance.",
            "Severely spotted leaves drop, reducing fruit size and sugar content.",
            "Small dark spots on peach skin that turn into deep, unsightly cracks."
        ],
        "organic_control": [
            "Apply organic copper sprays starting during bud swell and leaf fall.",
            "Use biobactericides containing Bacillus amyloliquefaciens."
        ],
        "chemical_control": [
            "Apply oxytetracycline (e.g., Mycoshield) at 7-10 day intervals during warm, wet weather."
        ],
        "prevention": [
            "Plant resistant peach cultivars (e.g., Redhaven, Biscoe, Challenger).",
            "Avoid excess nitrogen fertilization, which stimulates overly dense succulent growth."
        ],
        "severity_level": "Medium"
    },

    # ── PEPPER DISEASES ──────────────────────────────────────────────────────
    "Pepper,_bell___Bacterial_spot": {
        "crop": "Pepper",
        "disease_name": "Bacterial Spot",
        "cause": "Xanthomonas campestris pv. vesicatoria (bacteria)",
        "description": "Causes rapid spotting on pepper leaves and stems, resulting in severe defoliation and sunscald on bell peppers.",
        "symptoms": [
            "Small water-soaked green-yellow spots on leaves that turn dark brown.",
            "Foliage spots turn into dry raised lesions on leaf undersides.",
            "Leaves turn yellow and drop off; fruit shows scabby dark lesions."
        ],
        "organic_control": [
            "Apply organic copper hydroxide bactericides preventatively.",
            "Drench soil with compost tea to build beneficial root microbe defenses."
        ],
        "chemical_control": [
            "Use copper bactericides combined with mancozeb for enhanced spray synergy."
        ],
        "prevention": [
            "Use only certified pathogen-free pepper seeds.",
            "Avoid splash irrigation; maintain clean straw mulches around pepper beds."
        ],
        "severity_level": "Medium"
    }
}

# ── HEALTHY CROP ADVISORY TEMPLATES ──────────────────────────────────────────
# Used as highly positive, expert-level feedback when a leaf is classified as Healthy.

HEALTHY_CROP_ADVISORY = {
    "crop": "Healthy Host Plant",
    "disease_name": "Healthy & Pathogen Free",
    "cause": "Optimal Plant Vigor and Excellent Gardening Practices",
    "description": "Your crop leaf shows no active signs of fungal, bacterial, or viral disease! The cell walls are strong, color is rich, and transpiration is working perfectly.",
    "symptoms": [
        "Consistent, deep green foliage with uniform pigmentation.",
        "No active brown spotting, leaf yellowing, curling, or fuzzy mold.",
        "Strong, sturdy stems and leaves showing turgor pressure (no wilting)."
    ],
    "organic_control": [
        "Continue standard organic fertilization with well-aged compost or vermicompost tea.",
        "Apply neem oil or insecticidal soap only as a preventive measure if pest bugs appear."
    ],
    "chemical_control": [
        "None needed! Avoid spraying unnecessary chemical fungicides or pesticides to protect beneficial insects."
    ],
    "prevention": [
        "Maintain current watering routines (irrigate early in the morning at the soil level).",
        "Periodically check foliage undersides for early signs of spider mites or aphids.",
        "Ensure crops have excellent air circulation by keeping weeds down."
    ],
    "severity_level": "Healthy"
}

# ── DYNAMIC GENERATION FALLBACK ──────────────────────────────────────────────
# Automatically generates high-fidelity advisory details on-the-fly if a less common
# disease is classified, ensuring that the system is 100% robust for all 38 classes.

def get_crop_advisory(class_name):
    """
    Retrieves detailed expert advisory for a given class classification tag.
    Provides custom-tailored advice for healthy hosts and minor classes.
    """
    if not class_name:
        return HEALTHY_CROP_ADVISORY
        
    if "healthy" in class_name.lower():
        crop = class_name.split("___")[0].replace("_", " ").strip()
        adv = HEALTHY_CROP_ADVISORY.copy()
        adv["crop"] = crop
        adv["disease_name"] = f"Healthy {crop} Leaf"
        return adv
        
    if class_name in ADVISORY_DATABASE:
        return ADVISORY_DATABASE[class_name]
        
    # Smart Fallback Generator to ensure 100% class safety
    parts = class_name.split("___")
    crop = parts[0].replace("_", " ").strip().title()
    disease = parts[1].replace("_", " ").strip().title() if len(parts) > 1 else "Infection"
    
    return {
        "crop": crop,
        "disease_name": disease,
        "cause": f"Pathogenic crop infection affecting {crop} tissue",
        "description": f"An active case of {disease} has been identified on your {crop} crop. Prompt cultural controls and protective measures are recommended to halt spread.",
        "symptoms": [
            f"Atypical pigmentation, spotting, or leaf lesions on {crop} tissue.",
            "Wilted, curled, or prematurely yellowing foliage margins.",
            "Stunted growth or reduced yield capacity on infected plant zones."
        ],
        "organic_control": [
            "Apply copper-based organic fungicides or broad-spectrum horticultural oils.",
            "Prune off heavily spotted leaves and isolate the plant immediately."
        ],
        "chemical_control": [
            "Use general-purpose broad-spectrum fungicides according to label instructions.",
            "Consult with local agricultural extensions if the infection covers >15% of the canopy."
        ],
        "prevention": [
            "Water early in the morning at the base of the crop to avoid wet foliage.",
            "Sanitize all gardening tools with rubbing alcohol between tasks.",
            "Rotate crops and clear out dead crop debris in autumn."
        ],
        "severity_level": "Medium"
    }
