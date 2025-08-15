
import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Assalomu alaykum botga xush kelibsiz bot sizga har qanday meva va sabzavot haqida malumot beradi ')
        

@dp.message(Command('ananas'))
async def cmd_ananas(message: Message):
    await message.reply('Ananas tropik meva bo‘lib, shirin va nordon ta’mga ega.'
                        ' U sariq go‘shti bilan boy vitamin C manbai hisoblanadi. Ananas sharbat, salat va shirinliklarda ishlatiladi.'
                        ' Uning qobig‘i qattiq, ichi esa suvli. U immunitetni mustahkamlashga yordam beradi.')

@dp.message(F.text == 'anor')
async def cmd_anor(message: Message):
    await message.reply('Anor qizil donalari bilan mashhur, shirin-nordon ta’mli meva. U antioksidantlarga boy va yurak salomatligini qo‘llab-quvvatlaydi.'
                        ' Anor sharbat sifatida yoki salatlarda ishlatiladi. Uning qobig‘i yemaydigan qismi, donalari esa mazali.'
                        ' O‘zbekistonda anor ko‘pincha kuzda yig‘iladi.')

@dp.message(Command('apelsin'))
async def cmd_apelsin(message: Message):
    await message.answer('Anor qizil donalari bilan mashhur, shirin-nordon ta’mli meva. U antioksidantlarga boy va yurak salomatligini qo‘llab-quvvatlaydi.'
                         ' Anor sharbat sifatida yoki salatlarda ishlatiladi. Uning qobig‘i yemaydigan qismi, donalari esa mazali. '
                         'O‘zbekistonda anor ko‘pincha kuzda yig‘iladi.')

@dp.message(Command('banan'))
async def cmd_banan(message:Message):
    await message.reply('Banan uzun, yumshoq va shirin tropik meva. U kaliy va energiya manbai sifatida tanilgan.'
                        ' Banan smuzi, shirinlik yoki xom holda iste’mol qilinadi. Uning qobig‘i sariq va yemaydigan qismdir.'
                        ' Banan O‘zbekistonda import qilinadi.')

@dp.message(Command('dolana'))
async def cmd_dolana(message:Message):
    await message.reply('Dolana kichik, qizil yoki sariq meva bo‘lib, nordon ta’mli. U yurak faoliyatini yaxshilashga yordam beradi.'
                        ' Dolana choy, sharbat yoki quritilgan holda ishlatiladi. Uning donalari mayda va danagi bor. O‘zbekistonda dori sifatida ham tanilgan.')

@dp.message(Command('gilos'))
async def cmd_gilos(message:Message):
    await message.reply('Gilos qizil yoki qora rangli, shirin-nordon meva. U antioksidantlarga boy va yallig‘lanishga qarshi xususiyatlarga ega.'
                        ' Gilos xom, murabbo yoki shirinliklarda ishlatiladi. Uning danagi yemaydigan qismdir. O‘zbekistonda yozda mashhur.')

@dp.message(Command('kivi'))
async def cmd_kivi(message:Message):
    await message.reply('Kivi yashil go‘shtli, mayda urug‘li tropik meva. U C vitamini va tolalarga boy, immunitetni mustahkamlaydi.'
                        ' Kivi xom holda yoki smuzilarda iste’mol qilinadi. Uning qobig‘i yemaydi, lekin ba’zilar uni yeyishadi. O‘zbekistonda import qilinadi.')

@dp.message(Command('kokos'))
async def cmd_kokos(message:Message):
    await message.reply('Kokos tropik meva bo‘lib, ichidagi suv va go‘sht ishlatiladi. U kaliy va sog‘lom yog‘larga boy.'
                        ' Kokos sut, yog‘ yoki shirinliklarda qo‘llaniladi. Uning qobig‘i qattiq, ichi esa oq va mazali. Ekzotik meva sifatida tanilgan.')

@dp.message(Command('limon'))
async def cmd_limon(message:Message):
    await message.reply('Limon nordon ta’mli, sariq sitrus mevasi. U C vitamini manbai bo‘lib, immunitetni ko‘taradi.'
                        ' Limon sharbat, choy yoki taomlarga qo‘shiladi. Uning qobig‘i aromatik, go‘shti esa suvli. O‘zbekistonda yil davomida mavjud.')

@dp.message(Command('mango'))
async def cmd_mango(message:Message):
    await message.reply('Mango shirin va suvli tropik meva bo‘lib, sariq-narunji go‘shtga ega. U A, C va E vitaminlariga boy.'
                        ' Mango smuzi, salat yoki xom holda iste’mol qilinadi. Uning ta’mi boy va o‘ziga xos. O‘zbekistonda import qilinadi.')


@dp.message(Command('nok'))
async def cmd_nok(message:Message):
    await message.reply('Nok shirin va suvli meva bo‘lib, turli ranglarda bo‘ladi. U tolalar va C vitamini manbai hisoblanadi.'
                        ' Nok xom, pishirilgan yoki sharbat sifatida iste’mol qilinadi. Uning go‘shti yumshoq va ta’mi nozik. O‘zbekistonda yoz-kuzda mashhur.')


@dp.message(Command('olma'))
async def cmd_olma(message:Message):
    await message.reply('Olma eng keng tarqalgan meva bo‘lib, shirin yoki nordon ta’mli.'
                        ' U vitaminlar va tolalarga boy, hazm qilishni yaxshilaydi. Olma xom, pishirilgan yoki sharbat sifatida yeyiladi.'
                        ' Uning turlari rang va ta’m jihatidan xilma-xil. O‘zbekistonda yil davomida mavjud.')


@dp.message(Command('orik'))
async def cmd_orik(message:Message):
    await message.reply('O‘rik shirin va suvli, sariq-narunji meva. U A vitamini va tolalarga boy, ko‘rishni yaxshilaydi.'
                        ' O‘rik xom, quritilgan yoki murabbo sifatida iste’mol qilinadi. Uning danagi yemaydigan qismdir.'
                        ' O‘zbekistonda yozda pishadi.')


@dp.message(Command('qulupnay'))
async def cmd_qulupnay(message:Message):
    await message.reply('Qulupnay qizil, shirin va suvli meva. U C vitamini va antioksidantlarga boy.'
                        ' Qulupnay xom, murabbo yoki shirinliklarda ishlatiladi. Uning urug‘lari tashqarisida joylashgan, ta’mi o‘ziga xos.'
                        ' O‘zbekistonda bahorda pishadi.')


@dp.message(Command('shaftoli'))
async def cmd_shaftoli(message:Message):
    await message.reply('Shaftoli shirin, suvli va tukli qobqli meva. U A va C vitaminlariga boy, teri salomatligiga foydali.'
                        ' Shaftoli xom, kompot yoki shirinliklarda yeyiladi. Uning go‘shti sariq yoki oq bo‘ladi. O‘zbekistonda yozda mashhur.')


@dp.message(Command('uzum'))
async def cmd_uzum(message:Message):
    await message.reply('Uzum shirin yoki nordon ta’mli, kichik meva. U antioksidantlarga boy va sharob yoki mayiz uchun ishlatiladi.'
                        ' Uzum xom, quritilgan yoki sharbat sifatida yeyiladi. Uning turlari rang va ta’m jihatidan xilma-xil. O‘zbekistonda uzumchilik rivojlangan.')


@dp.message(Command('anjir'))
async def cmd_anjir(message:Message):
    await message.reply('Anjir shirin va yumshoq ta’mli, qora yoki yashil meva. U tolalar va kaliyga boy, hazm qilishni yaxshilaydi.'
                        ' Anjir xom yoki quritilgan holda yeyiladi. Uning go‘shti urug‘li va suvli. O‘zbekistonda yoz-kuzda pishadi.')


@dp.message(Command('malina'))
async def cmd_malina(message:Message):
    await message.reply('Malina shirin-nordon, qizil yoki sariq meva. U antioksidantlarga boy va yallig‘lanishga qarshi xususiyatlarga ega.'
                        ' Malina xom, murabbo yoki smuzilarda ishlatiladi. Uning go‘shti nozik va suvli. O‘zbekistonda yozda pishadi.')


@dp.message(Command('qovun'))
async def cmd_qovun(message:Message):
    await message.reply('Qovun shirin, suvli va yirik meva. U suv va kaliy manbai, yozda serinlantiradi.'
                        ' O‘zbekistonda yozda pishadi, xom yoki salatlarda ishlatiladi. Uning go‘shti sariq yoki oq bo‘ladi.'
                        ' O‘zbekistonda yozning sevimli mevasi.')



@dp.message(Command('bodring'))
async def cmd_bodring(message:Message):
    await message.reply('Bodring suvli, yashil va serinlantiruvchi sabzavot. U salatlarda xom holda yoki tuzlash uchun ishlatiladi.'
                        ' O‘zbekistonda yozda pishadi, C vitamini manbai. Uning ta’mi engil va qarsildoq. Bog‘larda va issiqxonalarda yetishtiriladi.')



@dp.message(Command('sabzi'))
async def cmd_sabzi(message:Message):
    await message.reply('Sabzi to‘q sariq, shirin va qattiq sabzavot. U A vitamini manbai, ko‘rish va teri salomatligiga foydali.'
                        ' O‘zbekistonda yil davomida pishadi, sho‘rva yoki salatlarda ishlatiladi. Uning ildizi suvli, barglari yemaydi. Bog‘larda keng tarqalgan.')


@dp.message(Command('kartoshka'))
async def cmd_kartoshka(message:Message):
    await message.reply('Kartoshka O‘zbekistonda asosiy sabzavotlardan biri. U kraxmalli, to‘yimli va turli taomlarda ishlatiladi.'
                        ' Yil davomida yetishtiriladi, qovuriladi, pishiriladi yoki sho‘rvaga qo‘shiladi. Uning ta’mi yumshoq va ko‘p qirrali.'
                        ' O‘zbek oshxonasida muhim o‘rin tutadi.')


@dp.message(Command('qovoq'))
async def cmd_qovoq(message:Message):
    await message.reply('Qovoq yirik, suvli va shirin ta’mli sabzavot. U tolalar va vitaminlarga boy, sho‘rva yoki pishiriqlarda ishlatiladi.'
                        ' O‘zbekistonda yoz-kuzda pishadi, qovuriladi yoki bug‘da pishiriladi. Uning go‘shti sariq, qobig‘i qattiq. O‘zbek oshxonasida mashhur.')



@dp.message(Command(''))
async def cmd_(message:Message):
    await message.reply('')



@dp.message(Command(''))
async def cmd_(message:Message):
    await message.reply('')




@dp.message(Command(''))
async def cmd_(message:Message):
    await message.reply('')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('\nGoodbye')

