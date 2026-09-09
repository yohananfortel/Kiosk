<script setup>
import { ref } from "vue";

const steps = ref([
  {
    title: "Крок 1: Вибір спеціальності",
    description:
      "Ознайомтеся з переліком спеціальностей нашого коледжу в інформаційному меню та оберіть ту, яка найбільше відповідає вашим інтересам та майбутнім кар'єрним цілям.",
    badge: "Початок",
    type: "start",
  },
  {
    title: "Крок 2: Підготовка документів",
    description:
      "Зберіть необхідний пакет документів: паспорт або свідоцтво про народження, ідентифікаційний код, документ про попередню освіту (з додатком), 4 фотокартки 3х4 та медичну довідку.",
    badge: "Важливо",
    type: "warning",
  },
  {
    title: "Крок 3: Подання заяви",
    description:
      "Зареєструйте свій електронний кабінет вступника та подайте заяву в електронній формі. За потреби зверніться до нашої приймальної комісії за технічною допомогою.",
    badge: "Онлайн",
    type: "info",
  },
  {
    title: "Крок 4: Співбесіда чи НМТ",
    description:
      "Пройдіть індивідуальну усну співбесіду або надайте результати Національного мультипредметного тесту (НМТ) відповідно до вимог обраної вами спеціальності.",
    badge: "Іспити",
    type: "danger",
  },
  {
    title: "Крок 5: Зарахування до коледжу",
    description:
      "Слідкуйте за рейтинговими списками. Після отримання рекомендації до зарахування виконайте вимоги та привітайте себе — ви офіційно студент найкращого коледжу!",
    badge: "Успіх",
    type: "success",
  },
]);
</script>

<template>
  <div class="applicant-map">
    <header class="applicant-map__header">
      <h2 class="applicant-map__title">Карта вступника: 5 кроків до успіху</h2>
      <p class="applicant-map__subtitle">
        Твій покроковий путівник для вступу до нашого закладу
      </p>
    </header>

    <div class="applicant-map__timeline">
      <div class="applicant-map__line"></div>

      <div class="applicant-map__steps">
        <div
          v-for="(step, index) in steps"
          :key="index"
          class="applicant-map__step"
        >
          <div class="applicant-map__number-zone">
            <div :class="['applicant-map__number', `applicant-map__number--${step.type}`]">
              <span class="applicant-map__digit">{{ index + 1 }}</span>
            </div>
          </div>

          <div class="applicant-map__card">
            <div class="applicant-map__card-header">
              <h3 class="applicant-map__card-title">{{ step.title }}</h3>
              <span :class="['applicant-map__badge', `applicant-map__badge--${step.type}`]">
                {{ step.badge }}
              </span>
            </div>
            <p class="applicant-map__card-desc">
              {{ step.description }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* ==========================================================================
   Блок: applicant-map (Карта вступника)
   Методологія: БЕМ
   ========================================================================== */

.applicant-map {
  max-width: 1100px;
  margin: 0 auto;
  padding: 20px;
  font-family: system-ui, -apple-system, sans-serif;
}

.applicant-map__header {
  text-align: center;
  margin-bottom: 40px;
}

.applicant-map__title {
  font-size: 2.8rem;
  font-weight: 800;
  color: #166534;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin: 0 0 10px 0;
}

.applicant-map__subtitle {
  font-size: 1.35rem;
  color: #64748b;
  margin: 0;
}

.applicant-map__timeline {
  position: relative;
  width: 100%;
  margin-top: 25px;
}

.applicant-map__line {
  position: absolute;
  left: 40px;
  top: 40px;
  bottom: 40px;
  width: 4px;
  background: linear-gradient(to bottom, #cbd5e1 50%, transparent 50%);
  background-size: 4px 16px;
  transform: translateX(-50%);
  z-index: 1;
}

.applicant-map__steps {
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.applicant-map__step {
  display: flex;
  align-items: center;
  position: relative;
  z-index: 2;
  opacity: 0;
  transform: translateY(30px);
  animation: stepFadeIn 0.5s ease forwards;
}

.applicant-map__step:nth-child(1) { animation-delay: 0.1s; }
.applicant-map__step:nth-child(2) { animation-delay: 0.2s; }
.applicant-map__step:nth-child(3) { animation-delay: 0.3s; }
.applicant-map__step:nth-child(4) { animation-delay: 0.4s; }
.applicant-map__step:nth-child(5) { animation-delay: 0.5s; }

.applicant-map__number-zone {
  width: 80px;
  display: flex;
  justify-content: center;
  flex-shrink: 0;
}

.applicant-map__number {
  width: 70px;
  height: 70px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 5px solid #ffffff;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
  transition: transform 0.25s ease;
}

.applicant-map__digit {
  color: #ffffff;
  font-size: 2.2rem;
  font-weight: 800;
}

.applicant-map__number--start { background: #00a53f; }
.applicant-map__number--warning { background: #f59e0b; }
.applicant-map__number--info { background: #3b82f6; }
.applicant-map__number--danger { background: #ef4444; }
.applicant-map__number--success { background: #10b981; }

.applicant-map__card {
  flex: 1;
  background: #f8fafc;
  border: 2px solid #e2e8f0;
  border-radius: 20px;
  padding: 22px 30px;
  margin-left: 25px;
  transition: all 0.25s ease;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.02);
}

.applicant-map__card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.applicant-map__card-title {
  font-size: 1.6rem;
  font-weight: 800;
  color: #1e293b;
  margin: 0;
}

.applicant-map__badge {
  padding: 6px 14px;
  border-radius: 30px;
  font-size: 0.95rem;
  font-weight: 700;
  text-transform: uppercase;
  color: #ffffff;
}

.applicant-map__badge--start { background: #00a53f; }
.applicant-map__badge--warning { background: #f59e0b; }
.applicant-map__badge--info { background: #3b82f6; }
.applicant-map__badge--danger { background: #ef4444; }
.applicant-map__badge--success { background: #10b981; }

.applicant-map__card-desc {
  font-size: 1.25rem;
  line-height: 1.55;
  color: #475569;
  margin: 0;
}

.applicant-map__step:hover .applicant-map__card {
  transform: translateX(8px);
  background: #ffffff;
  border-color: #00a53f;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
}

.applicant-map__step:hover .applicant-map__number {
  transform: scale(1.08);
}

@keyframes stepFadeIn {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
