import streamlit as st
import random
import time

# إعداد واجهة اللعبة
st.set_page_config(page_title="ردع العدوان: العبور", layout="centered")

# تهيئة المتغيرات التكتيكية (منظور الشخص الأول)
if 'tactical_state' not in st.session_state:
    st.session_state.tactical_state = "BREACH_PREP"  # نقطة البداية: التحضير للاقتحام
    st.session_state.ak47_mag = 30                  # مخزن الكلاشنكوف
    st.session_state.rpg_rounds = 2                 # قذائف الآر بي جي
    st.session_state.stamina = 100                  # طاقة الجسد والتركيز
    st.session_state.suppression = 0                # مستوى ضغط نيران العدو عليك
    st.session_state.logs = ["أنت الآن تجثو على ركبتيك خلف الساتر الترابي.. الغبار يملأ رِئتك."]

def add_tactical_log(text):
    st.session_state.logs.append(text)

# المؤشرات التكتيكية في الشريط الجانبي (منظور الشخص الأول)
st.sidebar.title("🪖 خوذة القتال - HUD")
st.sidebar.markdown("---")
st.sidebar.write(f"🔫 **سلاحك الرئيسي:** AK-47 ({st.session_state.ak47_mag}/30) طلقة")
st.sidebar.write(f"🚀 **السلاح الثقيل:** RPG-7 ({st.session_state.rpg_rounds}) قذائف")
st.sidebar.progress(st.session_state.stamina / 100, text=f"🫁 الأنفاس والتركيز: {st.session_state.stamina}%")
st.sidebar.progress(st.session_state.suppression / 100, text=f"💥 ضغط نيران العدو: {st.session_state.suppression}%")

st.sidebar.markdown("---")
st.sidebar.subheader("📡 اللاسلكي وصوت الفصيل:")
for log in reversed(st.session_state.logs[-4:]):
    st.sidebar.write(log)

# شروط الاستشهاد أو الفشل التكتيكي
if st.session_state.suppression >= 100:
    st.error("💀 أصابتك رصاصة قناص عطلت حركتك تماماً.. سقطت الكلاشنكوف من يدك وتوقف الإرسال.")
    if st.button("🔄 إعادة المحاولة واقتحام الساتر مجدداً"):
        st.session_state.clear()
        st.rerun()
    st.stop()

# الشاشة الرئيسية - رؤية اللاعب
st.title("👁️ منظور الشخص الأول: معركة العبور")
st.markdown("---")

# --- المشهد الأول: التحضير واقتحام خط الدفاع الأول ---
if st.session_state.tactical_state == "BREACH_PREP":
    st.subheader("🎵 صوت أزيز الرصاص فوق رأسك مباشرة")
    st.write("""
    يدك اليسرى تقبض بقوة على خشبة **الكلاشنكوف (AK-47)** الدافئة، وسبابتك اليمنى تلامس الزناد المعدني البارد. 
    بجانبك يلتفت إليك **أبو جعفر**، ملامحه مغطاة بالغبار، يضع يده على كتفك ويصرخ وسط ضجيج المدافع: 
    *"يا بطل! الدشمة (النقطة المحصنة) اللي أمامنا مباشرة عم تقطع الممر بنيران الرشاش الثقيل.. إذا ما سكتناها ما حدا ح يعبر! جهز حالك وثبت رجليك!"*
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗣️ اصرخ لـ أبو جعفر: 'غطيني!' وثبت الكلاشنكوف على الساتر للرمي"):
            st.session_state.ak47_mag -= 10
            st.session_state.suppression = max(0, st.session_state.suppression - 20)
            st.session_state.tactical_state = "FIRE_FIGHT"
            add_tactical_log("💥 سحبت أقسام الكلاشنكوف (كلاك!) وأطلقت دفعة تكتيكية أُجبرت رامي الرشاش على الاختباء.")
            st.rerun()
            
    with col2:
        if st.button("🚀 اسحب قاذف الـ RPG-7 الثقيل وضعه على كتفك الأيمن"):
            if st.session_state.rpg_rounds > 0:
                st.session_state.tactical_state = "RPG_AIM"
                add_tactical_log("🚀 رفعت القاذف.. الوزن ثقيل على كتفك، وبدأت بمحاذاة شعيرة الرمي نحو النافذة.")
                st.rerun()

# --- المشهد الثاني: تبادل النيران الكثيف بكلاشنكوف ---
elif st.session_state.tactical_state == "FIRE_FIGHT":
    st.subheader("🔥 اشتباك ناري مباشر - من خلف مسند السلاح")
    st.write("""
    أنت الآن تنظر عبر مسطرة المسافة لسلاحك. الرصاص يضرب الساتر أمامك ويتناثر التراب على وجهك. 
    مخزن سلاحك بدأ يفرغ، والعدو يعيد تذخير رشاشه الآن. **أبو جعفر** يصرخ بلاسلكي المجموعة: 
    *"المجموعة الثانية تقدمت من اليسار! اضرب الآن لشتت انتباههم!"*
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔫 رمي خاطف وسريع من فوق الساتر"):
            st.session_state.ak47_mag -= 15
            st.session_state.suppression += 30
            add_tactical_log("💥 ارتداد الكلاشنكوف قوي في كتفك! أصبت حامي الدشمة وتراجعوا للخلف.")
            st.session_state.tactical_state = "ROOM_BREACH"
            st.rerun()
            
    with col2:
        if st.button("🔄 انزل تحت الساتر، اضغط على زر قفل المخزن، واسحب مخزن جديد (تلقيم التكتيكي)"):
            st.session_state.ak47_mag = 30
            st.session_state.stamina = max(0, st.session_state.stamina - 10)
            add_tactical_log("🔊 (طق!.. كلاك!) قمت بتلقيم مخزن جديد بسرعة ونفذت مناورة هجومية.")
            st.rerun()

# --- المشهد الثالث: تسديد قاذف الآر بي جي ---
elif st.session_state.tactical_state == "RPG_AIM":
    st.subheader("🚀 قاذف RPG-7: لحظة الإطلاق القاتلة")
    st.write("""
    أنت الآن ترى الدشمة الإسمنتية عبر منظار القاذف. يدك تقبض على المقبض الصغير، ونزعت فتيل الأمان بأصابعك. 
    تسمع **أبو جعفر** يلتفت للخلف ويصرخ بأعلى صوته لتنبيه بقية الشباب: 
    *"لهبببب خلفي!!! ابعدوا عن ظهر القاذف!!"*
    الأجواء مشحونة، والثواني كأنها ساعات.
    """)
    
    if st.button("🔥 اضغط على زناد القاذف واطلق!"):
        st.session_state.rpg_rounds -= 1
        st.session_state.suppression = 0
        st.session_state.tactical_state = "ROOM_BREACH"
        add_tactical_log("🚀 (بومممم!) انطلقت القذيفة بصوت مرعب هز الأرض، وارتدت النيران خلفك مدمرة الدشمة كلياً!")
        st.rerun()

# --- المشهد الرابع: اقتحام الغرف والتطهير ---
elif st.session_state.tactical_state == "ROOM_BREACH":
    st.subheader("🚪 اقتحام المبنى الرئيسي - الغرف الداخلية")
    st.write("""
    الدفاعات انهارت! تقدمت راكضاً والكاميرا تهتز (محاكاة ركض الشخص الأول)، وصلت إلى الباب الخشبي المخلوع للمقر.
    تلتصق بجدار الباب من اليمين، و**أبو جعفر** يلتصق من اليسار ويمسك بقنبلة هجومية. 
    ينظر إليك، يومئ برأسه ويعد: *"واحد.. اثنين.. ثلاثة!"* ويرمي القنبلة للداخل. بعد الانفجار مباشرة، حان دورك للدخول أولاً!
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🥾 اقتحم الغرفة (منظور مسح الزوايا) واطلق النار على عناصر المقاومة المتبقية"):
            if st.session_state.ak47_mag >= 10:
                st.session_state.ak47_mag -= 10
                st.session_state.tactical_state = "TACTICAL_VICTORY"
                add_tactical_log("💥 دخلت ووجهت فوهة السلاح لليمين ثم لليسر، وسيطرت على الغرفة بالكامل.")
            else:
                st.session_state.suppression += 50
                add_tactical_log("⚠️ دخلت ومخزنك فارغ! اضطررت للتراجع للخلف وتحت غطاء نيران أبو جعفر.")
            st.rerun()
            
    with col2:
        if st.button("🗣️ اصرخ: 'تطهير الزاوية العمياء!' واجعل أبو جعفر يقتحم معك كتفاً بكتف"):
            st.session_state.tactical_state = "TACTICAL_VICTORY"
            add_tactical_log("🤝 اقتحمتما معاً بالتزامن، تم تصفية التهديد دون تعريض نفسك لخطر فردي.")
            st.rerun()

# --- مشهد النصر والعبور ---
elif st.session_state.tactical_state == "TACTICAL_VICTORY":
    st.balloons()
    st.success("🏆 تم تطهير الموقع الدفاعي بالكامل وعزل المحور!")
    st.write("""
    ### 🎖️ شاشة نهاية العبور التكتيكي (منظور الشخص الأول):
    تقف الآن داخل الغرفة المدمرة، الدخان يتصاعد من فوهة كلاشنكوفك الساخنة. 
    يأتي **أبو جعفر** ليربت على كتفك ويقول والابتسامة على وجهه: *"سلمت يداك يا بطل، لولا القذيفة وتغطيتك التكتيكية ما كنا عبرنا. الآن الطريق إلى دمشق أصبح مؤمناً بالكامل!"*
    
    أنزلت سلاحك، وتنفست الصعداء بعد ليلة قتال ملحمية عشت تفاصيلها بنفسك وبقراراتك.
    """)
    
    if st.button("🔄 العودة لنقطة الصفر وخوض السيناريو بخيارات أخرى"):
        st.session_state.clear()
        st.rerun()
