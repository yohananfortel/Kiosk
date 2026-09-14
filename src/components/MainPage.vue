<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const emit = defineEmits(['open-schedule']);

const currentDate = ref('');
const currentTimeStr = ref('');

const updateTime = () => {
  const now = new Date();
  
  const months = [
    'січня', 'лютого', 'березня', 'квітня', 'травня', 'червня',
    'липня', 'серпня', 'вересня', 'жовтня', 'листопада', 'грудня'
  ];
  
  const days = [
    'неділя', 'понеділок', 'вівторок', 'середа',
    'четвер', 'п\'ятниця', 'субота'
  ];

  const day = now.getDate();
  const month = months[now.getMonth()];
  const dayOfWeek = days[now.getDay()];
  
  const hours = now.getHours().toString().padStart(2, '0');
  const minutes = now.getMinutes().toString().padStart(2, '0');
  const seconds = now.getSeconds().toString().padStart(2, '0');

  currentDate.value = `${day} ${month}`;
  currentTimeStr.value = `${dayOfWeek} ${hours}:${minutes}:${seconds}`;
};

let timer;
onMounted(() => {
  updateTime();
  timer = setInterval(updateTime, 1000);
});

onUnmounted(() => {
  clearInterval(timer);
});
</script>

<template>
  <div class="main-page">
    <div class="main-page__top">
      <img
        src="https://ocsnau.net/wp-content/themes/ocsnau_v3/assets/images/logo_ukr_color.png?v=2"
        alt="Емблема коледжу"
        class="main-page__logo"
      />
    </div>
    
    <div class="main-page__middle">
      <div class="main-page__time-container">
        <div class="main-page__date">{{ currentDate }}</div>
        <div class="main-page__time">{{ currentTimeStr }}</div>
      </div>
    </div>
    
    <div class="main-page__bottom">
      <button class="main-page__help-btn" @click="emit('open-schedule')">
        <span class="main-page__help-icon">
          <svg viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M15.0233 6C15.9392 6 16.7412 6.55169 17.0984 7.39129C17.4557 8.2309 17.2796 9.18349 16.6322 9.85196L11.5833 15.0645L7.36783 10.849L8.78205 9.43482L11.5833 12.2361L15.2179 8.43482L15.0233 6Z" display="none"/>
            <path d="M12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z"/>
            <path d="M12 16.5V17M12 7V13"/>
          </svg>
        </span>
        Торкніться щоб отримати допомогу
      </button>
    </div>
  </div>
</template>

<style scoped>
.main-page {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  height: 100%;
  width: 100%;
  padding: 40px 20px;
  box-sizing: border-box;
}

.main-page__top {
  flex: 1;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding-top: 40px;
}

.main-page__logo {
  height: 160px;
  max-width: 100%;
  object-fit: contain;
  filter: drop-shadow(0 10px 20px rgba(0, 0, 0, 0.1));
}

.main-page__middle {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

.main-page__time-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 10px;
}

.main-page__date {
  font-size: 6.5rem;
  font-weight: 800;
  color: #064e3b;
  text-shadow: 0 4px 15px rgba(255, 255, 255, 0.8);
}

.main-page__time {
  font-size: 5.5rem;
  font-weight: 700;
  color: #064e3b;
  text-align: center;
  text-shadow: 0 4px 15px rgba(255, 255, 255, 0.8);
  letter-spacing: 2px;
}

.main-page__bottom {
  flex: 1;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  padding-bottom: 60px;
}

.main-page__help-btn {
  display: flex;
  align-items: center;
  gap: 16px;
  background: linear-gradient(135deg, #059669 0%, #047857 100%);
  color: white;
  border: none;
  border-radius: 100px;
  padding: 24px 60px;
  font-size: 2.2rem;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 20px 40px rgba(5, 150, 105, 0.3);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  text-transform: uppercase;
  letter-spacing: 1px;
}

.main-page__help-btn:active {
  transform: scale(0.95);
  box-shadow: 0 10px 20px rgba(5, 150, 105, 0.2);
}

.main-page__help-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.1); }
  100% { transform: scale(1); }
}
</style>
