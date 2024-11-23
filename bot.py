import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import yt_dlp

# إعدادات تسجيل الأخطاء
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# دالة /start التي ترحب بالمستخدم
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('مرحباً! أرسل لي رابط فيديو TikTok.')

# دالة لمعالجة الرابط وإرسال الفيديو
def get_tiktok_video(update: Update, context: CallbackContext) -> None:
    try:
        # استخراج الرابط من الرسالة
        url = update.message.text.split(' ')[1]

        # استخدام yt-dlp لتحميل الفيديو
        ydl_opts = {
            'quiet': True,
            'format': 'bestvideo+bestaudio/best',
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_url = info_dict.get('url', None)
            
            if video_url:
                update.message.reply_text(f'إليك رابط الفيديو المباشر: {video_url}')
            else:
                update.message.reply_text('لم أتمكن من تحميل الفيديو.')
    except IndexError:
        update.message.reply_text('يرجى إرسال رابط TikTok بشكل صحيح.')
    except Exception as e:
        update.message.reply_text(f'حدث خطأ أثناء معالجة الفيديو: {e}')

# إعداد التوكن الخاص بالبوت
def main():
    token = 'PUT_YOUR_BOT_API_KEY_HERE'  # استبدل بهذا التوكن الخاص بك
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    # إضافة معالج الأوامر
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("get_tiktok_video", get_tiktok
