#ملف مو لي تم نشر للافاده 

#『 مـصـدر 𝙵𝙰𝚁𝟹𝙾𝙽 𝚃𝙴𝙲𝙷』 
#@V_I_P_H7

import telebot
from telebot import types
import random
bot = telebot.TeleBot("7680410833:AAESNMhjnk__RSn1cwZB0Sj-4qMmqFfY3TU")

donkey = []
mute = []
lista = [

"اخر افلام شاهدتها",

"ما هيا عيوب  ؟ ",

" هل بتكراش ع حد في حياتك؟",

" ينفع نرتبط؟",

" ممكن توريني صوره بتحبها؟",

" ممكن نبقي صحااب ع الفيس؟",

"عندك كام اكس في حياتك؟ ",

"ينفع تبعتلي رقمك؟ ",

" ما تيجي اعزمني ع حاجه بحبها؟",

"ينفع احضنك؟ ",

"قولي ع اكبر غلطه ندمان عليهاا؟ ",

"عندك كام سنه؟ ",

" عامل بلوك لكام واحد عندك؟",

" قولي سر محدش يعرفه؟",

" عندك كام اكس في حياتك؟",

"بتعرف تقلش وتهزر؟ ",

" لونك المفضل هو؟",

"كتابك المفضل",

"هوايتك المفضله",

"علاقتك مع اهلك",

" ما السيء في هذه الحياة ؟ ",

"أجمل شيء حصل معك خلال هذا الاسبوع ؟ ",

"سؤال ينرفزك ؟ ",

" هل يعجبك  ؟؟ ",

" اكثر ممثل تحبه ؟ ",

"قد تخيلت شي في بالك وصار ؟ ",

"شيء عندك اهم من الناس ؟ ",

"تفضّل النقاش الطويل او تحب الاختصار ؟ ",

"وش أخر شي ضيعته؟ ",

"اي رايك في  ؟ ",

"كم مره حبيت؟ ",

" اكثر المتابعين عندك باي برنامج؟",

" اخر مره ضربت عشره كانت متى ؟",

" نسبه الندم عندك للي وثقت فيهم ؟",

"تحب ترتبط بكيرفي ولا فلات؟",

" جربت شعور احد يحبك بس انت مو قادر تحبه؟",

" تجامل الناس ولا اللي بقلبك على لسانك؟",

" عمرك ضحيت باشياء لاجل شخص م يسوى ؟",

"مغني تلاحظ أن صوته يعجب الجميع إلا أنت؟ ",

" اخر غلطات عمرك؟ ",

" مسلسل كرتوني له ذكريات جميلة عندك؟ ",

" ما أكثر تطبيق تقضي وقتك عليه؟ ",

" أول شيء يخطر في بالك إذا سمعت كلمة نجوم ؟ ",

" قدوتك من الأجيال السابقة؟ ",

" أكثر طبع تهتم بأن يتواجد في شريك/ة حياتك؟ ",

"أكثر حيوان تخاف منه؟ ",

" ما هي طريقتك في الحصول على الراحة النفسية؟ ",

" إيموجي يعبّر عن مزاجك الحالي؟ ",

" أكثر تغيير ترغب أن تغيّره في نفسك؟ ",

"أكثر شيء أسعدك اليوم؟ ",

"اي رايك في الدنيا دي ؟ ",

"ما هو أفضل حافز للشخص؟ ",

"ما الذي يشغل بالك في الفترة الحالية؟",

"اخر شيء ندمت عليه؟ ",

"شاركنا صورة احترافية من تصويرك؟ ",

"تتابع انمي؟ إذا نعم ما أفضل انمي شاهدته ",

"يرد عليك متأخر على رسالة مهمة وبكل برود، موقفك؟ ",

"نصيحه تبدا ب -لا- ؟ ",

"كتاب أو رواية تقرأها هذه الأيام؟ ",

"فيلم عالق في ذهنك لا تنساه مِن روعته؟ ",

"يوم لا يمكنك نسيانه؟ ",

"شعورك الحالي في جملة؟ ",

"كلمة لشخص بعيد؟ ",

"صفة يطلقها عليك الشخص المفضّل؟ ",

"أغنية عالقة في ذهنك هاليومين؟ ",

"أكلة مستحيل أن تأكلها؟ ",

"كيف قضيت نهارك؟ ",

"تصرُّف ماتتحمله؟ ",

"موقف غير حياتك؟ ",

"اكثر مشروب تحبه؟ ",

"القصيدة اللي تأثر فيك؟ ",

"متى يصبح الصديق غريب ",

"وين نلقى السعاده برايك؟ ",

"تاريخ ميلادك؟ ",

"قهوه و لا شاي؟ ",

"من محبّين الليل أو الصبح؟ ",

"حيوانك المفضل؟ ",

"كلمة غريبة ومعناها؟ ",

"كم تحتاج من وقت لتثق بشخص؟ ",

"اشياء نفسك تجربها؟ ",

"يومك ضاع على؟ ",

"كل شيء يهون الا ؟ ",

"اسم ماتحبه ؟ ",

"وقفة إحترام للي إخترع ؟ ",

"أقدم شيء محتفظ فيه من صغرك؟ ",

"كلمات ماتستغني عنها بسوالفك؟ ",

"وش الحب بنظرك؟ ",

"حب التملك في شخصِيـتك ولا ؟ ",

"تخطط للمستقبل ولا ؟ ",

"موقف محرج ماتنساه ؟ ",

"من طلاسم لهجتكم ؟ ",

"اعترف باي حاجه ؟ ",

"عبّر عن مودك بصوره ؟ ",

"اخر مره ضربت عشره كانت متى ؟",

"اسم دايم ع بالك ؟ ",

"اشياء تفتخر انك م سويتها ؟ ",

" لو بكيفي كان ؟ ",

  "أكثر جملة أثرت بك في حياتك؟ ",

  "إيموجي يوصف مزاجك حاليًا؟ ",

  "أجمل اسم بنت بحرف الباء؟ ",

  "كيف هي أحوال قلبك؟ ",

  "أجمل مدينة؟ ",

  "كيف كان أسبوعك؟ ",

  "شيء تشوفه اكثر من اهلك ؟ ",

  "اخر مره فضفضت؟ ",

  "قد كرهت احد بسبب اسلوبه؟ ",

  "قد حبيت شخص وخذلك؟ ",

  "كم مره حبيت؟ ",

  "اكبر غلطة بعمرك؟ ",

  "شنو رأيك بمطوري @pboty?",

  "نسبة النعاس عندك حاليًا؟ ",

  "شرايكم بمشاهير التيك توك؟ ",

  "ما الحاسة التي تريد إضافتها للحواس الخمسة؟ ",

  "اسم قريب لقلبك؟ ",

  "مشتاق لمطعم كنت تزوره قبل الحظر؟ ",

  "ما أول مشروع تتوقع أن تقوم بإنشائه إذا أصبحت مليونير؟ ",

  "أغنية عالقة في ذهنك هاليومين؟ ",

  "متى اخر مره قريت قران؟ ",

  "كم صلاة فاتتك اليوم؟ ",#V_I_P_H7

  "تفضل التيكن او السنقل؟ ",#V_I_P_H7

  "وش أفضل بوت برأيك؟ ",

"كم لك بالتلي؟ ",

"وش الي تفكر فيه الحين؟ ",

"هل تحب تيتو صاحب  ",

"كيف تشوف الجيل ذا؟ ",

"منشن شخص وقوله، تحبني؟ ",

"لو جاء شخص وعترف لك كيف ترده؟ ",

"مر عليك موقف محرج؟ ",

"وين تشوف نفسك بعد سنتين؟ ",

"وش اجمل لهجة تشوفها؟ ",

"قد سافرت؟ ",

"افضل مسلسل عندك؟ ",

"افضل فلم عندك؟ ",

"مين اكثر يخون البنات/العيال؟ ",

"متى حبيت؟ ",

  "بالعادة متى تنام؟ ",

  "شيء من صغرك ماتغير فيك؟ ",

  "شيء بسيط قادر يعدل مزاجك بشكل سريع؟ ",

  "تشوف الغيره انانيه او حب؟ ",

"حاجة تشوف نفسك مبدع فيها؟ ",

"اكثر شي يزعجك فيني؟",

  "مع او ضد : يسقط جمال المراة بسبب قبح لسانها؟ ",

  "عمرك بكيت على شخص مات في مسلسل ؟ ",

  "‏- هل تعتقد أن هنالك من يراقبك بشغف؟ ",

  "تدوس على قلبك او كرامتك؟ ",

  "اكثر لونين تحبهم مع بعض؟ ",

  "مع او ضد : النوم افضل حل لـ مشاكل الحياة؟ ",

  "سؤال دايم تتهرب من الاجابة عليه؟ ",

  "تحبني ولاتحب الفلوس؟ ",

  "العلاقه السريه دايماً تكون حلوه؟ ",

  "لو أغمضت عينيك الان فما هو أول شيء ستفكر به؟ ",

"كيف ينطق الطفل اسمك؟ ",

  "ما هي نقاط الضعف في شخصيتك؟ ",

  "اكثر كذبة تقولها؟ ",

  "تيكن ولا اضبطك؟ ",

  "اطول علاقة كنت فيها مع شخص؟ ",

  "قد ندمت على شخص؟ ",

  "وقت فراغك وش تسوي؟ ",

  "عندك أصحاب كثير؟ ولا ينعد بالأصابع؟ ",

  "حاط نغمة خاصة لأي شخص؟ ",

  "وش اسم شهرتك؟ ",

  "أفضل أكلة تحبه لك؟ ",

"عندك شخص تسميه ثالث والدينك؟ ",

  "عندك شخص تسميه ثالث والدينك؟ ",

  "اذا قالو لك تسافر أي مكان تبيه وتاخذ معك شخص واحد وين بتروح ومين تختار؟ ",

  "أطول مكالمة كم ساعة؟ ",

  "اريد جواب صريح، تمراس العادة السرية؟ ،جاوب اذا كنت ولد او بنت",

  "تحب الحياة الإلكترونية ولا الواقعية؟ ",

  "كيف حال قلبك ؟ بخير ولا مكسور؟ ",

  "أطول مدة نمت فيها كم ساعة؟ ",

  "تقدر تسيطر على ضحكتك؟ ",

  "أول حرف من اسم الحب؟ ",

  "تحب تحافظ على الذكريات ولا تمسحه؟ ",

  "اسم اخر شخص زعلك؟ ",

"وش نوع الأفلام اللي تحب تتابعه؟ ",

  "أنت انسان غامض ولا الكل يعرف عنك؟ ",

  "لو الجنسية حسب ملامحك وش بتكون جنسيتك؟ ",

  "عندك أخوان او خوات من الرضاعة؟ ",

  "إختصار تحبه؟ ",

  "إسم شخص وتحس أنه كيف؟ ",

  "وش الإسم اللي دايم تحطه بالبرامج؟ ",

  "وش برجك؟ ",

  "تتابع افلام محرمة؟",

  "لو يجي عيد ميلادك تتوقع يجيك هدية؟ ",

  "اجمل هدية جاتك وش هو؟ ",

  "الصداقة ولا الحب؟ ",

"الصداقة ولا الحب؟ ",

  "الغيرة الزائدة شك؟ ولا فرط الحب؟ ",

  "قد حبيت شخصين مع بعض؟ وانقفطت؟ ",

  "وش أخر شي ضيعته؟ ",

  "قد ضيعت شي ودورته ولقيته بيدك؟ ",

  "تؤمن بمقولة اللي يبيك مايحتار فيك؟ ",

  "سبب وجوك بالتليجرام؟ ",

  "تراقب شخص حاليا؟ ",

  "عندك معجبين ولا محد درا عنك؟ ",

  "لو نسبة جمالك بتكون بعدد شحن جوالك كم بتكون؟ ",

  "أنت محبوب بين الناس؟ ولاكريه؟ ",

"كم عمرك؟ ",

  "لو يسألونك وش اسم امك تجاوبهم ولا تسفل فيهم؟ ",

  "تؤمن بمقولة الصحبة تغنيك الحب؟ ",

  "وش مشروبك المفضل؟ ",

  "تعرف/ين جوني سينس؟",

  "قد جربت الدخان بحياتك؟ وانقفطت ولا؟ ",

  "أفضل وقت للسفر؟ الليل ولا النهار؟ ",

  "انت من النوع اللي تنام بخط السفر؟ ",

  "عندك حس فكاهي ولا نفسية؟ ",

  "تبادل الكراهية بالكراهية؟ ولا تحرجه بالطيب؟ ",

  "أفضل ممارسة بالنسبة لك؟ ",

  "لو قالو لك تتخلى عن شي واحد تحبه بحياتك وش يكون؟ ",

"لو احد تركك وبعد فتره يحاول يرجعك بترجع له ولا خلاص؟ ",

  "برأيك كم العمر المناسب للزواج؟ ",

  "اذا تزوجت بعد كم بتخلف عيال؟ ",

  "فكرت وش تسمي أول اطفالك؟ ",

  "من الناس اللي تحب الهدوء ولا الإزعاج؟ ",

  "الشيلات ولا الأغاني؟ ",

  "عندكم شخص مطوع بالعايلة؟ ",

  "تتقبل النصيحة من اي شخص؟ ",

  "اذا غلطت وعرفت انك غلطان تحب تعترف ولا تجحد؟ ",

  "جربت شعور احد يحبك بس انت مو قادر تحبه؟ ",

  "دايم قوة الصداقة تكون بإيش؟ ",

"أفضل البدايات بالعلاقة بـ وش؟ ",

  "وش مشروبك المفضل؟ او قهوتك المفضلة؟ ",

  "تحب تتسوق عبر الانترنت ولا الواقع؟ ",

  "انت من الناس اللي بعد ماتشتري شي وتروح ترجعه؟ ",

  "أخر مرة بكيت متى؟ وليش؟ ",

  "عندك الشخص اللي يقلب الدنيا عشان زعلك؟ ",

  "أفضل صفة تحبه بنفسك؟ ",

  "كلمة تقولها للوالدين؟ ",

  "أنت من الناس اللي تنتقم وترد الاذى ولا تحتسب الأجر وتسامح؟ ",

  "كم عدد سنينك بالتليجرام؟ ",

  "تحب تعترف ولا تخبي؟ ",

"انت من الناس الكتومة ولا تفضفض؟ ",

  "أنت بعلاقة حب الحين؟ ",

  "عندك اصدقاء غير جنسك؟ ",

  "أغلب وقتك تكون وين؟ ",

  "لو المقصود يقرأ وش بتكتب له؟ ",

  "تحب تعبر بالكتابة ولا بالصوت؟ ",

  "عمرك كلمت فويس احد غير جنسك؟ ",

  "لو خيروك تصير مليونير ولا تتزوج الشخص اللي تحبه؟ ",

  "لو عندك فلوس وش السيارة اللي بتشتريها؟ ",

  "كم أعلى مبلغ جمعته؟ ",

  "جربت تصرف فلوس في الحرام؟",

  "اذا شفت احد على غلط تعلمه الصح ولا تخليه بكيفه؟ ",

"قد جربت تبكي فرح؟ وليش؟ ",

"تتوقع إنك بتتزوج اللي تحبه؟ ",

  "ما هو أمنيتك؟ ",

  "وين تشوف نفسك بعد خمس سنوات؟ ",

  "لو خيروك تقدم الزمن ولا ترجعه ورا؟ ",

  "لعبة قضيت وقتك فيه بالحجر المنزلي؟ ",

  "تحب تطق الميانة ولا ثقيل؟ ",

  "باقي معاك للي وعدك ما بيتركك؟ ",

  "اول ماتصحى من النوم مين تكلمه؟ ",

  "عندك الشخص اللي يكتب لك كلام كثير وانت نايم؟ ",

  "قد قابلت شخص تحبه؟ وولد ولا بنت؟ ",

"اذا قفطت احد تحب تفضحه ولا تستره؟ ",

  "كلمة للشخص اللي يسب ويسطر؟ ",

  "اية من القران تؤمن فيه؟ ",

  "تحب تعامل الناس بنفس المعاملة؟ ولا تكون أطيب منهم؟ ",

"حاجة ودك تغيرها هالفترة؟ ",

  "كم فلوسك حاليا وهل يكفيك ام لا؟ ",

  "وش لون عيونك الجميلة؟ ",

  "من الناس اللي تتغزل بالكل ولا بالشخص اللي تحبه بس؟ ",

  "اذكر موقف ماتنساه بعمرك؟ ",

  "وش حاب تقول للاشخاص اللي بيدخل حياتك؟ ",

  "ألطف شخص مر عليك بحياتك؟ ",

"انت من الناس المؤدبة ولا نص نص؟ ",

  "كيف الصيد معاك هالأيام ؟ وسنارة ولاشبك؟ ",

  "لو الشخص اللي تحبه قال بدخل حساباتك بتعطيه ولا تكرشه؟ ",

  "أكثر شي تخاف منه بالحياه وش؟ ",

  "اكثر المتابعين عندك باي برنامج؟ ",

  "متى يوم ميلادك؟ ووش الهدية اللي نفسك فيه؟ ",

  "قد تمنيت شي وتحقق؟ ",

  "قلبي على قلبك مهما صار لمين تقولها؟ ",

  "وش نوع جوالك؟ واذا بتغيره وش بتأخذ؟ ",

  "كم حساب عندك بالتليجرام؟ ",

  "متى اخر مرة كذبت؟ ",

"كذبت في الاسئلة اللي مرت عليك قبل شوي؟ ",

  "تجامل الناس ولا اللي بقلبك على لسانك؟ ",

  "قد تمصلحت مع أحد وليش؟ ",

  "وين تعرفت على الشخص اللي حبيته؟ ",

  "قد رقمت او احد رقمك؟ ",

  "وش أفضل لعبته بحياتك؟ ",

  "أخر شي اكلته وش هو؟ ",

  "حزنك يبان بملامحك ولا صوتك؟ ",

  "لقيت الشخص اللي يفهمك واللي يقرا افكارك؟ ",

  "فيه شيء م تقدر تسيطر عليه ؟ ",

  "منشن شخص متحلطم م يعجبه شيء؟ ",

"اكتب تاريخ مستحيل تنساه ",

  "شيء مستحيل انك تاكله ؟ ",

  "تحب تتعرف على ناس جدد ولا مكتفي باللي عندك ؟ ",

  "انسان م تحب تتعامل معاه ابداً ؟ ",

  "شيء بسيط تحتفظ فيه؟ ",

  "فُرصه تتمنى لو أُتيحت لك ؟ ",

  "شيء مستحيل ترفضه ؟. ",

  "لو زعلت بقوة وش بيرضيك ؟ ",

  "تنام بـ اي مكان ، ولا بس غرفتك ؟ ",

  "ردك المعتاد اذا أحد ناداك ؟ ",

  "مين الي تحب يكون مبتسم دائما ؟ ",

" إحساسك في هاللحظة؟ ",

  "وش اسم اول شخص تعرفت عليه فالتلقرام ؟ ",

  "اشياء صعب تتقبلها بسرعه ؟ ",

  "شيء جميل صار لك اليوم ؟ ",

  "اذا شفت شخص يتنمر على شخص قدامك شتسوي؟ ",

  "يهمك ملابسك تكون ماركة ؟ ",

  "ردّك على شخص قال (أنا بطلع من حياتك؟ ",

  "مين اول شخص تكلمه اذا طحت بـ مصيبة ؟ ",

  "تشارك كل شي لاهلك ولا فيه أشياء ما تتشارك؟ ",

  "كيف علاقتك مع اهلك؟ رسميات ولا ميانة؟ ",

  "عمرك ضحيت باشياء لاجل شخص م يسوى ؟ ",

  "اكتب سطر من اغنية او قصيدة جا فـ بالك ؟ ",

  "شيء مهما حطيت فيه فلوس بتكون مبسوط ؟ ",

  "مشاكلك بسبب ؟ ",

  "نسبه الندم عندك للي وثقت فيهم ؟ ",

  "اكثر شيء تحس انه مات ف مجتمعنا؟ ",

  "لو صار سوء فهم بينك وبين شخص هل تحب توضحه ولا تخليه كذا  لان مالك خلق توضح ؟ ",

  "كم عددكم بالبيت؟ ",

  "عادي تتزوج من برا القبيلة؟ ",

 "أجمل شي بحياتك وش هو؟ ",
]

@bot.message_handler(commands=['users'])
def user_bot(message):
    file = open('userss.txt','r')
    count = len(file.readlines())
    bot.send_message(message.chat.id, f"عدد مستخدمين البوت : {count}")

def ex_id(id):
    result = False
    file = open('userss.txt','r')
    for line in file:
        if line.strip()==id:
            result = True
    file.close()
    return result

@bot.message_handler(commands=['orders'])
def order(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"""<strong>
اوامر الحماية : 
-------------------------------------------------
استخدم امر "طرد" لطرد العضو من المجموعة

استخدم امر "الحظر" ل حظر العضو من المجموعة
استخدم امر "الغاء الحظر "الغاء الحظر" ل الغاء حظر العضو من المجموعة

استخدم امر "كتم" لكتم العضو في المجموعة
استخدم امر "الغاء الكتم" ل الغاء كتم العضو في المجموعة
-------------------------------------------------

الالعاب الي موجودة بالبوت : 
-------------------------------------------------
1 - لعبة بولينغ
2 - لعبة كرة القدم
3 - لعبة كرة سلة
4 - لعبة قمار
5 - لعبة تصويب
6 - كت
-------------------------------------------------
</strong>""", parse_mode='html', reply_to_message_id=message.message_id)

@bot.message_handler(commands=['start'])
def start(message):
    comm = types.InlineKeyboardMarkup(row_width=1)
    private = types.InlineKeyboardButton(url='https://t.me/DRR44', text='المطور - Programmer')
    chaanel = types.InlineKeyboardButton(url='https://t.me/BXX55', text='قناة المطور - Chaanel Programmer')
    comm.add(private,chaanel)
    m = message.chat.id
    if message.chat.type == 'private':
        idu = message.from_user.id
        f = open('userss.txt', 'a')
        if (not ex_id(str(idu))):
            f.write("{}\n".format(idu))
            f.close()
            name = message.from_user.first_name
            user = message.from_user.username
            ph = f'https://t.me/{user}'
            bot.send_photo(m, ph, f"""
ارفعني بكروبك واكتب تفعيل
ارسل امر /users : لمعرفة عدد مستخدمين البوت
ارسل امر /orders : معرفة اوامر البوت
""", parse_mode='Markdown', reply_to_message_id=message.message_id, reply_markup=comm)
        else:
            name = message.from_user.first_name
            user = message.from_user.username
            ph = f'https://t.me/{user}'
            bot.send_photo(m, ph, f"""
ارفعني بكروبك واكتب تفعيل
ارسل امر /users : لمعرفة عدد مستخدمين البوت
ارسل امر /orders : معرفة اوامر البوت
                        """, parse_mode='Markdown', reply_to_message_id=message.message_id, reply_markup=comm)
    else:
        username = message.from_user.username
        ph = f'https://t.me/{username}'
        bot.send_photo(m, ph, f"""
        ارفعني بكروبك واكتب تفعيل
        ارسل امر /users : لمعرفة عدد مستخدمين البوت
        ارسل امر /orders : معرفة اوامر البوت
                                """, parse_mode='Markdown', reply_to_message_id=message.message_id, reply_markup=comm)

@bot.message_handler(func=lambda message:True)
def boting(message):
    chat_id = message.chat.id
    adcon = ['creator', 'administrator']
    messag = message.text
    if messag =='طرد':
        if bot.get_chat_member(chat_id, message.from_user.id).status in adcon:
            name = message.reply_to_message.from_user.first_name
            bot.kick_chat_member(chat_id, message.reply_to_message.from_user.id)
            user = message.reply_to_message.from_user.username
            idd = message.reply_to_message.from_user.id
            id_user = str('-> @' + str(user) + ' - ' + '( <code>' + str(idd) + '</code> )')
            open(f'{chat_id}-kick.txt', 'a').write(f'{id_user}\n')
            bot.send_message(chat_id, f'''
المستخدم : [{name}](t.me/{user})
تم طرده من المجموعة .
''', parse_mode='markdown', disable_web_page_preview=True, reply_to_message_id=message.message_id)
        else:
            bot.send_message(chat_id, 'هذا الامر يخص الادمن او المالك .', reply_to_message_id=message.message_id)
    if messag =='المطرودين':
        kicks = open(f'{chat_id}-kick.txt','r').read()
        bot.send_message(chat_id, f'''
ملاحضة : لا يمكنك التعديل على هذه القائمة لانها تشمل كل الاعضاء الذي تم طردهم من المجموعة

{kicks}             

''', reply_to_message_id=message.message_id, parse_mode='html')
    if messag == 'كتم':
        if bot.get_chat_member(chat_id, message.from_user.id).status in adcon:
            name = message.json['reply_to_message']['from']['first_name']
            username = message.json['reply_to_message']['from']['username']
            id = message.json['reply_to_message']['from']['id']
            if id in mute:
                bot.reply_to(message, f'''**
العضو : [{name}](t.me/{username})
مكتوم سابقا .
            **''', parse_mode='markdown', disable_web_page_preview=True)
            else:
                name = message.json['reply_to_message']['from']['first_name']
                username = message.json['reply_to_message']['from']['username']
                id = message.json['reply_to_message']['from']['id']
                mute.append(id)
                user = message.reply_to_message.from_user.username
                idd = message.reply_to_message.from_user.id
                id_user = str('-> @' + str(user) + ' - ' + '( <code>' + str(idd) + '</code> )')
                open(f'{chat_id}-mute.txt', 'a').write(f'{id_user}\n')
                bot.reply_to(message, f'''**
العضو : [{name}](t.me/{username})
تم كتمه في المجموعة .
                        **''', parse_mode='markdown', disable_web_page_preview=True)
                print(mute)
        else:
            bot.reply_to(message, '<strong>هذا الامر يخص الادمن او المالك</strong>', parse_mode='html')

    if message.json['from']['id'] in mute:
        bot.delete_message(message.chat.id, message_id=message.message_id)
    if messag == 'الغاء الكتم':
        if bot.get_chat_member(chat_id, message.from_user.id).status in adcon:
            name = message.json['reply_to_message']['from']['first_name']
            username = message.json['reply_to_message']['from']['username']
            id = message.json['reply_to_message']['from']['id']
            mute.remove(id)
            bot.reply_to(message, f'''**
العضو : [{name}](t.me/{username})
تم الغاء كتمه في المجموعة .
                    **''', parse_mode='markdown', disable_web_page_preview=True)
            print(mute)
        else:
            bot.reply_to(message, '<strong>هذا الامر يخص الادمن او المالك</strong>', parse_mode='html')
    if messag=="المكتومين":
        mutes = open(f'{chat_id}-mute.txt','r').read()
        bot.send_message(chat_id, f'''
ملاحضة : لا يمكنك التعديل على هذه القائمة لانها تشمل كل الاعضاء الذي تم كتمهم في المجموعة

{mutes}             

''', reply_to_message_id=message.message_id, parse_mode='html')
    if messag=='حظر':
        if bot.get_chat_member(chat_id, message.from_user.id).status in adcon:
            name = message.reply_to_message.from_user.first_name
            bot.ban_chat_member(chat_id, message.reply_to_message.from_user.id)
            user = message.reply_to_message.from_user.username
            idd = message.reply_to_message.from_user.id
            id_user = str('-> @' + str(user) + ' - ' + '( <code>' + str(idd) + '</code> )')
            open(f'{chat_id}-ban.txt', 'a').write(f'{id_user}\n')
            bot.send_message(chat_id, f'''
المستخدم : [{name}](t.me/{user})
تم حظره من المجموعة .
        ''', parse_mode='markdown', disable_web_page_preview=True, reply_to_message_id=message.message_id)
        else:
            bot.send_message(chat_id, 'هذا الامر يخص الادمن او المالك .', reply_to_message_id=message.message_id)
    # Developer Bot - Naruto
    # Channel Developer - BXX55
    # User Developer - DRR44
    if message=='الغاء الحظر':
        if bot.get_chat_member(chat_id, message.from_user.id).status in adcon:
            name = message.reply_to_message.from_user.first_name
            bot.unban_chat_member(chat_id, message.reply_to_message.from_user.id)
            user = message.reply_to_message.from_user.username
            bot.send_message(chat_id, f'''
المستخدم : [{name}](t.me/{user})
تم الغاء حظره من المجموعة .
''', parse_mode='markdown', disable_web_page_preview=True, reply_to_message_id=message.message_id)
        else:
            bot.send_message(chat_id, 'هذا الامر يخص الادمن او المالك .', reply_to_message_id=message.message_id)
    if messag=='المحظورين':
        bans = open(f'{chat_id}-ban.txt', 'r').read()
        bot.send_message(chat_id, f'''
ملاحضة : لا يمكنك التعديل على هذه القائمة لانها تشمل كل الاعضاء الذي تم حظرهم في المجموعة

{bans}             

''', reply_to_message_id=message.message_id, parse_mode='html')
    if messag=='كت':
        bot.send_message(chat_id, f'<strong>{random.choice(lista)}</strong>', parse_mode='html', reply_to_message_id=message.message_id)

    if messag =='رفع مطي':
        user = message.reply_to_message.from_user.username
        name = message.reply_to_message.from_user.first_name
        idd = message.reply_to_message.from_user.id
        id_user = str('-> @' + str(user) + ' - ' + '( <code>' + str(idd) + '</code> )')
        open(f'{chat_id}-donkey.txt', 'a').write(f'{id_user}\n')
        donkey.append(idd)
        bot.send_message(chat_id, f'''
المستخدم : [{name}](t.me/{user})
رفعته مطي في المجموعة .
''', parse_mode='markdown', reply_to_message_id=message.message_id)
    if messag=='تنزيل مطي':
        if message.reply_to_message.from_user.id in donkey:
            user = message.reply_to_message.from_user.username
            name = message.reply_to_message.from_user.first_name
            donkey.remove(message.reply_to_message.from_user.id)
            bot.send_message(chat_id, f'''
المستخدم : [{name}](t.me/{user})
نزلته من قائمة المطايا في المجموعة .
''', parse_mode='markdown', reply_to_message_id=message.message_id)
        else:
            user = message.reply_to_message.from_user.username
            name = message.reply_to_message.from_user.first_name
            bot.send_message(chat_id, f'''
المستخدم : [{name}](t.me/{user})
مو مطي في المجموعة .
''', parse_mode='markdown', reply_to_message_id=message.message_id)
    if messag=='المطايا':
        donkeys = open(f'{chat_id}-donkey.txt', 'r').read()
        bot.send_message(chat_id, f'''
{donkeys}
''', parse_mode='html', reply_to_message_id=message.message_id)
    if messag=='بولينغ':
        # Developer Bot - Naruto
        # Channel Developer - BXX55
        # User Developer - DRR44
        bot.send_dice(chat_id, emoji='🎳', disable_notification=True)
    if messag=='تصويب':
        # Developer Bot - Naruto
        # Channel Developer - BXX55
        # User Developer - DRR44
        bot.send_dice(chat_id, emoji='🎯', disable_notification=True)
    if messag=='كرة قدم':
        bot.send_dice(chat_id, emoji='⚽', disable_notification=True)
    if messag=='قمار':
        # Developer Bot - Naruto
        # Channel Developer - BXX55
        # User Developer - DRR44
        bot.send_dice(chat_id, emoji='🎰', disable_notification=True)
    if messag=='كرة سلة':
        bot.send_dice(chat_id, emoji='🏀', disable_notification=True)
        # Developer Bot - Naruto
        # Channel Developer - BXX55
        # User Developer - DRR44
@bot.message_handler(content_types=['left_chat_member'])
def dele(message):
    bot.delete_message(message.chat.id, message_id=message.message_id)


#V_I_P_H7
bot.infinity_polling()

#ملف مو لي تم نشر للافاده 

#『 مـصـدر 𝙵𝙰𝚁𝟹𝙾𝙽 𝚃𝙴𝙲𝙷』 
#@V_I_P_H7
