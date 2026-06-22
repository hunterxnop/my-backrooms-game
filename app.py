import streamlit as st

st.set_page_config(page_title="The Backrooms", layout="centered")

if 'stage' not in st.session_state: st.session_state.stage = "intro"

st.title("👁️ The Backrooms: الهروب")
st.markdown("---")

if st.session_state.stage == "intro":
    st.write("### 🎬 الفصل الأول: السقوط خارج الواقع")
    st.write("فتحت عينيك لتجد نفسك في المستوى 0: جدران صفراء لا تنتهي، وسجاد رطب، وأزيز مصابيح مزعج.")
    if st.button("👁️ ابدأ بالتحرك وحاول الهروب"):
        st.session_state.stage = "escape"
        st.rerun()

elif st.session_state.stage == "escape":
    st.success("🎉 تهانينا! نجحت في اختراق الجدار والهروب!")
    if st.button("🔄 إعادة اللعبة"):
        st.session_state.stage = "intro"
        st.rerun()
