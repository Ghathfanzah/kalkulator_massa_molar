# Judul
st.set_page_config(page_title="Kalkulator Massa Molar", page_icon="🧪")
st.title("🧪 Kalkulator Massa Molar")
st.markdown("Masukkan rumus kimia (misal: `H2O`, `NaCl`, `C6H12O6`) untuk menghitung massa molarnya.")

# Fungsi untuk parsing rumus
import re

def parse_formula(formula):
    pattern = r'([A-Z][a-z]?)(\d*)'
    matches = re.findall(pattern, formula)
    return [(elem, int(count) if count else 1) for elem, count in matches]

# Fungsi menghitung massa molar
def calculate_molar_mass(formula):
    parsed = parse_formula(formula)
    total_mass = 0.0
    for symbol, count in parsed:
        try:
            atomic_mass = getattr(elements, symbol).mass
            total_mass += atomic_mass * count
        except AttributeError:
            st.error(f"Elemen tidak dikenali: {symbol}")
            return None
    return total_mass

# Input dari user
formula = st.text_input("Masukkan Rumus Kimia:", "")

if formula:
    molar_mass = calculate_molar_mass(formula)
    if molar_mass:
        st.success(f"Massa molar dari {formula} adalah **{molar_mass:.3f} g/mol**")
