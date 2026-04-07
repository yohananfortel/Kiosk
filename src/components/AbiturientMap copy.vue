<template>
  <div class="max-w-4xl mx-auto p-6 bg-white rounded-xl shadow-lg">
    <header class="text-center mb-10">
      <h2 class="text-3xl font-bold text-slate-800 uppercase tracking-wide">
        Карта вступника: 5 кроків до успіху
      </h2>
      <p class="text-slate-500 mt-2">Твій путівник для вступу до нашого коледжу</p>
    </header>

    <div class="relative">
      <div class="absolute left-8 top-0 h-full w-0.5 bg-blue-100 hidden md:block"></div>

      <div class="space-y-8">
        <div 
          v-for="(step, index) in steps" 
          :key="index" 
          class="relative flex flex-col md:flex-row items-start md:items-center group"
        >
          <div 
            class="flex items-center justify-center w-16 h-16 rounded-full border-4 border-white shadow-md z-10 transition-transform duration-300 group-hover:scale-110"
            :class="step.color"
          >
            <span class="text-white font-bold text-2xl">{{ index + 1 }}</span>
          </div>

          <div class="mt-4 md:mt-0 md:ml-10 flex-1 p-5 rounded-lg border border-slate-100 hover:border-blue-200 hover:shadow-md transition-all bg-slate-50">
            <h3 class="text-xl font-bold text-slate-700 mb-2">{{ step.title }}</h3>
            <p class="text-slate-600 leading-relaxed">
              {{ step.description }}
            </p>
            <div v-if="step.deadline" class="mt-3 text-sm font-semibold text-blue-600">
              📅 Термін: {{ step.deadline }}
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="mt-12 p-6 bg-blue-50 rounded-xl border-l-4 border-blue-500">
      <h4 class="font-bold text-blue-800 mb-2 italic">Порада від приймальної комісії:</h4>
      <p class="text-blue-700 text-sm">
        Не зволікайте з реєстрацією електронного кабінету! Перевірте наявність усіх оригіналів документів заздалегідь, щоб уникнути черг в останні дні прийому.
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const steps = ref([
  {
    title: 'Реєстрація електронного кабінету',
    description: 'Створіть особистий кабінет вступника на офіційному порталі. Завантажте фотокартку та додаток до атестата.',
    deadline: 'з 1 липня',
    color: 'bg-blue-500'
  },
  {
    title: 'Подача електронної заяви',
    description: 'Оберіть наш коледж та бажану спеціальність у переліку. Вкажіть пріоритетність та додайте мотиваційний лист.',
    deadline: 'до середини липня',
    color: 'bg-indigo-500'
  },
  {
    title: 'Вступні випробування або розгляд документів',
    description: 'Пройдіть співбесіду, творчий конкурс або дочекайтеся результатів розгляду мотиваційних листів залежно від обраної спеціальності.',
    deadline: 'згідно з графіком',
    color: 'bg-purple-500'
  },
  {
    title: 'Рекомендація до зарахування',
    description: 'Знайдіть своє прізвище у списках рекомендованих на бюджет або контракт, які з’являться в особистому кабінеті.',
    deadline: 'кінець липня / початок серпня',
    color: 'bg-teal-500'
  },
  {
    title: 'Підтвердження вибору та зарахування',
    description: 'Принесіть оригінали документів до коледжу або підтвердіть вибір за допомогою ЕЦП/Дія.Підпис. Вітаємо, ви — студент!',
    deadline: 'протягом 3-5 днів після рекомендації',
    color: 'bg-green-500'
  }
]);
</script>

<style scoped>
/* Додаткові стилі для плавності анімації за потреби */

/* Плавна поява елементів при завантаженні */
.space-y-8 > div {
  animation: fadeInUp 0.6s ease forwards;
  opacity: 0;
}

/* Затримка анімації для кожного кроку, щоб вони з'являлися по черзі */
.space-y-8 > div:nth-child(1) { animation-delay: 0.1s; }
.space-y-8 > div:nth-child(2) { animation-delay: 0.2s; }
.space-y-8 > div:nth-child(3) { animation-delay: 0.3s; }
.space-y-8 > div:nth-child(4) { animation-delay: 0.4s; }
.space-y-8 > div:nth-child(5) { animation-delay: 0.5s; }

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Стилізація сполучної лінії (пунктирний ефект) */
.relative div.absolute.left-8 {
  background: linear-gradient(to bottom, #dbeafe 50%, transparent 50%);
  background-size: 1px 15px; /* Створює ефект пунктиру */
}

/* Додатковий ефект при наведенні на картку кроку */
.group:hover .flex-1 {
  transform: translateX(8px);
  background-color: #ffffff;
  border-left: 4px solid currentColor; /* Колір підтягнеться з контексту, якщо додати динамічно */
}

/* Спеціальний стан для іконок (кіл) */
.group:hover .z-10 {
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

/* Адаптивність для дуже малих екранів */
@media (max-width: 640px) {
  header h2 {
    font-size: 1.5rem;
  }
  
  .w-16 {
    width: 3rem;
    height: 3rem;
    font-size: 1.25rem;
  }
}

/* Ефект "світіння" для поради від комісії */
.bg-blue-50 {
  position: relative;
  overflow: hidden;
}

.bg-blue-50::after {
  content: "";
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(255,255,255,0.4) 0%, transparent 70%);
  pointer-events: none;
}

</style>