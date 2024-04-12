<template>
    <!-- test mode -->
      <div id="alert-1" class="flex items-center p-4 mb-4 text-red-600 rounded-lg dark:bg-gray-800 dark:text-blue-400" role="alert">
        <svg class="flex-shrink-0 w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
          <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z"/>
        </svg>
        <span class="sr-only">Info</span>
        <div class="ms-3 text-sm font-medium">
          Test rejimida ishlamoqda. Xatolar haqida <a href="#" class="font-semibold underline hover:no-underline">bizga</a> habar bering
        </div>
          <button type="button" class="ms-auto -mx-1.5 -my-1.5 bg-blue-50 text-blue-500 rounded-lg focus:ring-2 focus:ring-blue-400 p-1.5 hover:bg-blue-200 inline-flex items-center justify-center h-8 w-8 dark:bg-gray-800 dark:text-blue-400 dark:hover:bg-gray-700" data-dismiss-target="#alert-1" aria-label="Close">
            <span class="sr-only">Close</span>
            <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
            </svg>
        </button>
      </div>
    <!-- test mode -->
  <!-- header -->
  <header class="bg-gray-700">
    <div class="mx-auto max-w-screen-xl px-4 py-8 sm:px-6 sm:py-12 lg:px-8">
      <div class="sm:flex sm:items-center sm:justify-between">
        <div class="text-center sm:text-left">
          <h1 class="text-2xl font-bold text-gray-900 sm:text-3xl">Ishlar yaxshimi? Tog'a holamlar tuzukmi?</h1>

          <p class="mt-1.5 text-sm text-gray-500">Birov bilmidigan habar yozish kerakmi, kettik 🎉</p>
        </div>

        <div class="mt-4 flex flex-col gap-4 sm:mt-0 sm:flex-row sm:items-center">




          <!-- Modal toggle -->
          <button data-modal-target="default-modal" data-modal-toggle="default-modal"
            class="block text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
            type="button">
            Nima bu?
          </button>

          <!-- Main modal -->
          <div id="default-modal" tabindex="-1" aria-hidden="true"
            class="hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
            <div class="relative p-4 w-full max-w-2xl max-h-full">
              <!-- Modal content -->
              <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
                <!-- Modal header -->
                <div class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600">
                  <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
                    Qonun qoidalar
                  </h3>
                  <button type="button"
                    class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white"
                    data-modal-hide="default-modal">
                    <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                      viewBox="0 0 14 14">
                      <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6" />
                    </svg>
                    <span class="sr-only">Ortga</span>
                  </button>
                </div>
                <!-- Modal body -->
                <div class="p-4 md:p-5 space-y-4">
                  <p class="text-base leading-relaxed text-gray-500 dark:text-gray-400">
                    Kalit so'z kiriting. Quyida esa matn yozing. Tizim sizga matnni shifrlangan ko'rinishini qaytaradi.
                    Siz shifrlarngan matnni do'stlaringiz, tanishlaringizga yuborishingiz mumkin. Do'stlaringizga kalit
                    so'zni aytsangiz, ular shifrni o'qiy olishadi. Aks holda hech qachon siz yozgan matnni tarjima qila
                    olishmaydi
                  </p>
                  <p class="text-base leading-relaxed text-gray-500 dark:text-gray-400">
                    Axloqsiz so'zlar, har qanday O'zbekiston qonunchiligiga tahdid soladigan so'zlar yozish taqiqlanadi.
                    Farosatni ishlatib, do'stlar tanishlar bilan gaplashing
                  </p>
                </div>
                <!-- Modal footer -->
                <div class="flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b dark:border-gray-600">
                  <button data-modal-hide="default-modal" type="button"
                    class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Ha
                    bo'pti</button>
                  <button data-modal-hide="default-modal" type="button"
                    class="py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700">Yo'g'e</button>
                </div>
              </div>
            </div>
          </div>

          <a href="https://t.me/mehmonov_husniddin"
            class="block rounded-lg bg-indigo-600 px-5 py-3 text-sm font-medium text-white transition hover:bg-indigo-700 focus:outline-none focus:ring text-center">
            Aloqa
          </a>
        </div>
      </div>


    </div>
  </header>
  <!-- header -->

  <!-- main  -->
  <main>

    <div class="  mx-auto sm:w-9 md:w-1/4  lg:w-1/2 w-80  ">

      <div class="mt-3">
        <label for="key" class="block text-xs font-medium text-gray-700 dark:text-gray-200">
          Kalit so'z
        </label>

        <input type="text" id="key" v-model="key" placeholder="Ishonchliroq kalit so'z yozing"
          class=" mt-1 w-full rounded-md border-gray-200 shadow-sm sm:text-sm  dark:border-gray-700 dark:bg-gray-800 dark:text-white " />
      </div>

      <div class="mt-4">
        <label for="text" class="block text-xs font-medium text-gray-700 dark:text-gray-200">
          Matn
        </label>
        <textarea id="text" class="mt-2 w-full rounded-lg border-gray-200 align-top shadow-sm sm:text-sm" rows="4"
          maxlength="1000" v-model="text" placeholder="Shu yerda matn yoki shifrni joylang"></textarea>
        <button @click="encryptText" class="bg-blue-700 p-5 w-full mt-4 rounded font-bold text-white">Shifrlash</button>
        <button @click="decryptText" class="bg-blue-700 p-5 w-full mt-4 rounded font-bold text-white">Shifrdan ozod
          etish</button>
      </div>

    </div>
  </main>
  <!-- main  -->
  <div class="w-2/3 mx-auto mt-10 bg-white overflow-auto rounded-md p-3 mb-3">
    <p @click="copyToClipboard(encryptedText)" class="my-2">Shifrlangan matn: {{ encryptedText }}</p>
    <p class="my-2">Shifrlanmagan matn: {{ decryptedText }}</p>
  </div>



</template>


<script>
import { onMounted } from 'vue';
import { initFlowbite } from 'flowbite';


import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      key: '',
      text: '',
      encryptedText: '',
      decryptedText: ''
    }
  },
  methods: {
    encryptText() {
      axios.get(`http://127.0.0.1:8000/encrypt/${this.key}/${this.text}`)
        .then(response => {
          this.encryptedText = response.data;
        })
        .catch(error => {
          console.error(error);
          alert('Xatolik yuz berdi');
        });
    },
    decryptText() {
      axios.get(`http://127.0.0.1:8000/decrypt/${this.key}/${this.text}`)
        .then(response => {
          this.decryptedText = response.data;
        })
        .catch(error => {
          console.error(error);
          alert('Xatolik yuz berdi');
        });
    },
    copyToClipboard(text) {
  if (this.key && text) { // Agar kalit va matn mavjud bo'lsa
    const message = `Bu sizning kalit so'zingiz *${this.key}*. Bu esa shifrlangan matn *${text}* . Siz kalit va matn orqali ushbu habarni o'qishingiz mumkin`;
    navigator.clipboard.writeText(message);
    alert('Nusxalandi');
    window.open('https://t.me/share/url?url=' + encodeURIComponent(message));
  } else {
    alert('Kalit yoki matn mavjud emas. Iltimos, ularni kiriting va qayta urinib ko\'ring.');
  }
}
  }

}

</script>
