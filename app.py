import streamlit as st
import pandas as pd

PACKAGING_DATABASE = [

    {
        "material": "PET",
        "oxygen_barrier": 3,
        "moisture_barrier": 4,
        "light_protection": 1,
        "strength": 5,
        "temperature": 4,
        "recyclability": 4,
        "cost": 5,
        "weight": 4
    },

    {
        "material": "HDPE",
        "oxygen_barrier": 3,
        "moisture_barrier": 5,
        "light_protection": 2,
        "strength": 5,
        "temperature": 4,
        "recyclability": 4,
        "cost": 5,
        "weight": 4
    },

    {
        "material": "PP",
        "oxygen_barrier": 3,
        "moisture_barrier": 5,
        "light_protection": 1,
        "strength": 4,
        "temperature": 5,
        "recyclability": 4,
        "cost": 5,
        "weight": 4
    },

    {
        "material": "Glass",
        "oxygen_barrier": 5,
        "moisture_barrier": 5,
        "light_protection": 3,
        "strength": 2,
        "temperature": 5,
        "recyclability": 5,
        "cost": 2,
        "weight": 1
    },

    {
        "material": "Aluminium",
        "oxygen_barrier": 5,
        "moisture_barrier": 5,
        "light_protection": 5,
        "strength": 4,
        "temperature": 5,
        "recyclability": 5,
        "cost": 3,
        "weight": 3
    },

    {
        "material": "Paperboard",
        "oxygen_barrier": 2,
        "moisture_barrier": 1,
        "light_protection": 4,
        "strength": 3,
        "temperature": 2,
        "recyclability": 5,
        "cost": 5,
        "weight": 4
    },

    {
        "material": "Kraft Paper Pouch",
        "oxygen_barrier": 2,
        "moisture_barrier": 2,
        "light_protection": 4,
        "strength": 3,
        "temperature": 2,
        "recyclability": 4,
        "cost": 4,
        "weight": 5
    },

    {
        "material": "High-Barrier Pouch",
        "oxygen_barrier": 5,
        "moisture_barrier": 5,
        "light_protection": 5,
        "strength": 4,
        "temperature": 4,
        "recyclability": 2,
        "cost": 4,
        "weight": 5
    },

    {
        "material": "Compostable Biopolymer",
        "oxygen_barrier": 3,
        "moisture_barrier": 3,
        "light_protection": 2,
        "strength": 3,
        "temperature": 3,
        "recyclability": 2,
        "cost": 2,
        "weight": 5
    }

]

FOOD_REQUIREMENTS = {

    "Dry Food": {
        "moisture": 5,
        "oxygen": 3,
        "light": 3,
        "temperature": 2
    },

    "Chips / Snacks": {
        "moisture": 5,
        "oxygen": 5,
        "light": 4,
        "temperature": 2
    },

    "Coffee": {
        "moisture": 5,
        "oxygen": 5,
        "light": 5,
        "temperature": 2
    },

    "Spices": {
        "moisture": 4,
        "oxygen": 4,
        "light": 5,
        "temperature": 2
    },

    "Pickle / Acidic Food": {
        "moisture": 5,
        "oxygen": 4,
        "light": 3,
        "temperature": 3
    },

    "Edible Oil": {
        "moisture": 3,
        "oxygen": 5,
        "light": 5,
        "temperature": 3
    },

    "Beverage": {
        "moisture": 5,
        "oxygen": 4,
        "light": 3,
        "temperature": 3
    },

    "Hot-Fill Food": {
        "moisture": 5,
        "oxygen": 4,
        "light": 3,
        "temperature": 5
    },

    "Ready-to-Eat Food": {
        "moisture": 4,
        "oxygen": 3,
        "light": 2,
        "temperature": 4
    }

}

def get_product_requirements(product):

    product = product.lower().strip()

    st.subheader("🔬 Product Intelligence")

    st.write(
        "Tell PACKWISE the characteristics of your product. "
        "These characteristics are used to calculate packaging requirements."
    )

    col1, col2 = st.columns(2)

    with col1:

        moisture_sensitivity = st.slider(
            "💧 Moisture Sensitivity",
            1,
            5,
            3,
            help="1 = not sensitive, 5 = highly sensitive"
        )

        oxygen_sensitivity = st.slider(
            "🌬️ Oxygen Sensitivity",
            1,
            5,
            3,
            help="1 = not sensitive, 5 = highly sensitive"
        )

    with col2:

        light_sensitivity = st.slider(
            "☀️ Light Sensitivity",
            1,
            5,
            3,
            help="1 = not sensitive, 5 = highly sensitive"
        )

        temperature_sensitivity = st.slider(
            "🌡️ Temperature Sensitivity",
            1,
            5,
            3,
            help="1 = not sensitive, 5 = highly sensitive"
        )

    return {
        "moisture": moisture_sensitivity,
        "oxygen": oxygen_sensitivity,
        "light": light_sensitivity,
        "temperature": temperature_sensitivity
    }

# PRODUCT-MATERIAL COMPATIBILITY ENGINE

def calculate_compatibility(product, material):

    product_name = str(product).lower().strip()

    # Acidic products
    acidic_products = [
        "tomato",
        "tomato sauce",
        "ketchup",
        "pickle",
        "lemon",
        "lemon juice",
        "orange",
        "orange juice",
        "vinegar",
        "tamarind"
    ]

    # Oil products
    oily_products = [
        "oil",
        "edible oil",
        "cooking oil",
        "ghee",
        "butter"
    ]

    # Moisture-sensitive products
    moisture_sensitive = [
        "chips",
        "biscuits",
        "cookies",
        "flour",
        "cereal",
        "spices",
        "powder",
        "dry food"
    ]

    # Oxygen-sensitive products
    oxygen_sensitive = [
        "coffee",
        "nuts",
        "dry fruits",
        "chips",
        "snacks",
        "spices"
    ]

    # ---------- ACIDIC PRODUCTS ----------
    if any(x in product_name for x in acidic_products):

        if material == "Aluminium":
            return 20, "Low compatibility for acidic product"

        if material in ["Glass", "HDPE", "PP", "PET"]:
            return 100, "Good compatibility for acidic product"

        return 70, "Conditional compatibility"

    # ---------- OILY PRODUCTS ----------
    if any(x in product_name for x in oily_products):

        if material in ["Glass", "HDPE", "PET", "PP"]:
            return 100, "Good compatibility for oily product"

        return 70, "Conditional compatibility"

    # ---------- MOISTURE-SENSITIVE PRODUCTS ----------
    if any(x in product_name for x in moisture_sensitive):

        if material in ["HDPE", "PP", "High-Barrier Pouch", "PET"]:
            return 100, "Good compatibility for moisture-sensitive product"

    # ---------- OXYGEN-SENSITIVE PRODUCTS ----------
    if any(x in product_name for x in oxygen_sensitive):

        if material in ["High-Barrier Pouch", "Glass"]:
            return 100, "Good oxygen-barrier candidate"

    # Default
    return 80, "No major compatibility restriction detected"

def calculate_food_protection(food):

    requirements = FOOD_REQUIREMENTS[food]

    results = []

    for package in PACKAGING_DATABASE:

        moisture_score = (
            package["moisture_barrier"]
            * requirements["moisture"]
        )

        oxygen_score = (
            package["oxygen_barrier"]
            * requirements["oxygen"]
        )

        light_score = (
            package["light_protection"]
            * requirements["light"]
        )

        temperature_score = (
            package["temperature"]
            * requirements["temperature"]
        )

        total = (
            moisture_score
            + oxygen_score
            + light_score
            + temperature_score
        )

        results.append({
            "Material": package["material"],
            "Food Protection Score": round(total, 1)
        })

    return pd.DataFrame(results)

def calculate_context_score(package, climate, transport):

    score = 0

    if climate == "Hot / Humid":
        score += package["moisture_barrier"] * 10
        score += package["temperature"] * 10

    elif climate == "Hot / Dry":
        score += package["temperature"] * 10
        score += package["light_protection"] * 5

    elif climate == "Monsoon / Very Humid":
        score += package["moisture_barrier"] * 15
        score += package["strength"] * 5

    else:
        score += 50

    if transport == "Sea Freight":
        score += package["strength"] * 10
        score += package["moisture_barrier"] * 5

    elif transport == "Long Distance Road Transport":
        score += package["strength"] * 10

    elif transport == "Regional Road Transport":
        score += package["strength"] * 7

    elif transport == "Air Freight":
        score += package["strength"] * 7

    else:
        score += package["strength"] * 3

    return score

def calculate_sustainability(package):

    recycling = package["recyclability"] * 10

    weight = package["weight"] * 5

    return recycling + weight

def generate_recommendations(
    food,
    requirements,
    climate,
    transport,
    priority,
    budget,
    recycling,
    storage,
    shelf_life
):

    results = []

    # Different priorities change the decision.
    if priority == "Maximum Protection":
        weights = {
            "food": 0.35,
            "context": 0.25,
            "sustainability": 0.10,
            "cost": 0.05,
            "shelf": 0.25
        }

    elif priority == "Low Environmental Impact":
        weights = {
            "food": 0.25,
            "context": 0.15,
            "sustainability": 0.40,
            "cost": 0.05,
            "shelf": 0.15
        }

    elif priority == "Low Cost":
        weights = {
            "food": 0.25,
            "context": 0.15,
            "sustainability": 0.10,
            "cost": 0.35,
            "shelf": 0.15
        }

    else:
        weights = {
            "food": 0.30,
            "context": 0.25,
            "sustainability": 0.20,
            "cost": 0.10,
            "shelf": 0.15
        }

    for package in PACKAGING_DATABASE:

        # --------------------------------
        # 1. PRODUCT PROTECTION
        # --------------------------------

        moisture_fit = (
            package["moisture_barrier"]
            * requirements["moisture"]
        )

        oxygen_fit = (
            package["oxygen_barrier"]
            * requirements["oxygen"]
        )

        light_fit = (
            package["light_protection"]
            * requirements["light"]
        )

        temperature_fit = (
            package["temperature"]
            * requirements["temperature"]
        )

        maximum_food = (
            5 * requirements["moisture"]
            + 5 * requirements["oxygen"]
            + 5 * requirements["light"]
            + 5 * requirements["temperature"]
        )

        food_raw = (
            moisture_fit
            + oxygen_fit
            + light_fit
            + temperature_fit
        )

        food_score = (food_raw / maximum_food) * 100

        # --------------------------------
        # 2. CONTEXT SCORE
        # --------------------------------

        context = 30

        if climate == "Hot / Humid":
            context += package["moisture_barrier"] * 7
            context += package["temperature"] * 5

        elif climate == "Hot / Dry":
            context += package["temperature"] * 7
            context += package["light_protection"] * 3

        elif climate == "Monsoon / Very Humid":
            context += package["moisture_barrier"] * 8
            context += package["strength"] * 4

        else:
            context += package["strength"] * 3

        if transport == "Long Distance Road Transport":
            context += package["strength"] * 8

        elif transport == "Regional Road Transport":
            context += package["strength"] * 6

        elif transport == "Sea Freight":
            context += package["strength"] * 6
            context += package["moisture_barrier"] * 4

        elif transport == "Air Freight":
            context += package["strength"] * 5

        else:
            context += package["strength"] * 4

        if storage == "Frozen":
            context += package["temperature"] * 5

        elif storage == "Refrigerated":
            context += package["temperature"] * 3

        elif storage == "Hot Warehouse":
            context += package["temperature"] * 7

        else:
            context += package["strength"] * 2

        context_score = min(context, 100)

        # --------------------------------
        # 3. SUSTAINABILITY
        # --------------------------------

        sustainability = (
            package["recyclability"] * 15
            + package["weight"] * 4
        )

        if recycling == "Strong":
            sustainability += package["recyclability"] * 2

        elif recycling == "Limited":
            sustainability += package["recyclability"]

        sustainability_score = min(sustainability, 100)

        # --------------------------------
        # 4. COST FIT
        # --------------------------------

        if budget == "Tight":
            cost_score = package["cost"] * 20

        elif budget == "Flexible":
            cost_score = 55 + package["cost"] * 8

        else:
            cost_score = package["cost"] * 18

        cost_score = min(cost_score, 100)

        # --------------------------------
        # 5. SHELF LIFE
        # --------------------------------

        barrier_strength = (
            package["oxygen_barrier"]
            + package["moisture_barrier"]
            + package["light_protection"]
        )

        shelf_score = (
            barrier_strength / 15
        ) * 100

        if shelf_life > 180:
            shelf_score += package["strength"] * 3

        elif shelf_life > 90:
            shelf_score += package["strength"] * 2

        else:
            shelf_score += package["strength"]

        shelf_score = min(shelf_score, 100)

        # 6. PRODUCT-MATERIAL COMPATIBILITY

        compatibility_score, compatibility_reason = calculate_compatibility(
        food,
        package["material"]
        )

        compatibility_multiplier = compatibility_score / 100

        # --------------------------------
        # 6. FINAL SCORE
        # --------------------------------

        final_score = (
    food_score * weights["food"]
    + context_score * weights["context"]
    + sustainability_score * weights["sustainability"]
    + cost_score * weights["cost"]
    + shelf_score * weights["shelf"]
)

     # Compatibility acts as a safety/fit filter
        final_score = final_score * compatibility_multiplier

        results.append({

            "Material": package["material"],

            "Compatibility": round(compatibility_score, 1),
            "Compatibility Reason": compatibility_reason,

            "Food Protection": round(
                food_score, 1
            ),

            "Context Fit": round(
                context_score, 1
            ),

            "Sustainability": round(
                sustainability_score, 1
            ),

            "Cost Fit": round(
                cost_score, 1
            ),

            "Shelf-Life Fit": round(
                shelf_score, 1
            ),

            "Final Score": round(
                final_score, 1
            ),

            "Moisture Barrier": package[
                "moisture_barrier"
            ],

            "Oxygen Barrier": package[
                "oxygen_barrier"
            ],

            "Light Protection": package[
                "light_protection"
            ],

            "Strength": package[
                "strength"
            ],

            "Temperature Resistance": package[
                "temperature"
            ],

            "Recyclability": package[
                "recyclability"
            ]

        })

    results = pd.DataFrame(results)

    results = results.sort_values(
        by="Final Score",
        ascending=False
    )

    results = results.reset_index(
        drop=True
    )

    results.insert(
        0,
        "Rank",
        range(1, len(results) + 1)
    )

    return results


st.set_page_config(
    page_title="PACKWISE AI",
    page_icon="📦",
    layout="wide"
)

st.title("📦 PACKWISE AI")
st.subheader("Context-Aware Packaging Decision Engine")

st.write(
    "PACKWISE AI evaluates food characteristics, storage, "
    "transportation, climate, user priorities and sustainability "
    "to recommend suitable packaging."
)

st.divider()

st.header("🍱 Food Profile")

st.header("🍱 Food / Product Profile")

food = st.text_input(
    "Enter your product",
    placeholder="Example: chocolate, medicine, detergent, biscuits, shampoo..."
)

if food.strip() == "":
    st.info("👆 Enter any product name to continue.")
    st.stop()

st.success(f"Product entered: {food}")

shelf_life = st.slider(
    "Target Shelf Life (days)",
    min_value=1,
    max_value=730,
    value=90
)

st.write("Selected food:", food)
st.write("Target shelf life:", shelf_life, "days")

st.divider()

st.header("👤 User Requirements")

priority = st.selectbox(
    "What is your main priority?",
    [
        "Balanced",
        "Maximum Protection",
        "Low Environmental Impact",
        "Low Cost"
    ]
)

budget = st.selectbox(
    "Budget",
    [
        "Tight",
        "Normal",
        "Flexible"
    ]
)

recycling = st.selectbox(
    "Local recycling infrastructure",
    [
        "Strong",
        "Limited",
        "Uncertain"
    ]
)

st.divider()

st.header("🌍 Context")

storage = st.selectbox(
    "Storage condition",
    [
        "Ambient",
        "Refrigerated",
        "Frozen",
        "Hot Warehouse"
    ]
)

transport = st.selectbox(
    "Transportation",
    [
        "Short Local Delivery",
        "Regional Road Transport",
        "Long Distance Road Transport",
        "Air Freight",
        "Sea Freight"
    ]
)

climate = st.selectbox(
    "Climate",
    [
        "Cool / Dry",
        "Hot / Dry",
        "Hot / Humid",
        "Monsoon / Very Humid"
    ]
)

st.divider()

if st.button("🚀 ANALYZE PACKAGING"):

    requirements = get_product_requirements(food)

    results = generate_recommendations(
       food,
       requirements,
       climate,
       transport,
       priority,
       budget,
       recycling,
       storage,
       shelf_life
    )

    best = results.iloc[0]

    st.divider()

    st.header("🏆 PACKWISE AI Recommendation")

    st.success(
        f"Recommended Packaging: {best['Material']}"
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Final Score",
        f"{best['Final Score']}"
    )

    col2.metric(
        "Food Protection",
        f"{best['Food Protection']}"
    )

    col3.metric(
        "Context Fit",
        f"{best['Context Fit']}"
    )

    col4.metric(
        "Sustainability",
        f"{best['Sustainability']}"
    )

    st.subheader("📊 Packaging Ranking")

    st.dataframe(
        results,
        use_container_width=True,
        hide_index=True
    )
    st.subheader("🧪 Material Evidence")

    material_evidence = results[
    [
        "Material",
        "Moisture Barrier",
        "Oxygen Barrier",
        "Light Protection",
        "Strength",
        "Temperature Resistance",
        "Recyclability"
    ]
    ]

    st.dataframe(
    material_evidence,
    use_container_width=True,
    hide_index=True
    )

    st.subheader("🥇 Top 3 Packaging Options")

    top_three = results.head(3)[
    [
        "Rank",
        "Material",
        "Food Protection",
        "Context Fit",
        "Sustainability",
        "Cost Fit",
        "Shelf-Life Fit",
        "Final Score"
    ]
    ]

    st.dataframe(
    top_three,
    use_container_width=True,
    hide_index=True
    )

    st.subheader("📈 Packaging Score Comparison")

    chart_data = results.set_index("Material")["Final Score"]

    st.bar_chart(chart_data)

    st.subheader("🧠 Why did PACKWISE choose this material?")

    st.subheader("🔎 Decision Evidence")

    st.write(
    "The recommendation is based on the following measurable "
    "prototype criteria:"
   )

    evidence_columns = [
    "Material",
    "Food Protection",
    "Context Fit",
    "Sustainability",
    "Cost Fit",
    "Shelf-Life Fit",
    "Final Score"
    ]

    st.dataframe(
    results[evidence_columns],
    use_container_width=True,
    hide_index=True
    )

    st.info(
        f"PACKWISE selected {best['Material']} "
        f"because it achieved the highest overall score "
        f"for the selected food, climate, transportation "
        f"conditions and user priority."
    )