<script setup>
import Tabs from './components/Tabs.vue';
import Speciality from './components/Speciality.vue'; 
import WellcomeToTheCollege from './components/WellcomeToTheCollege.vue'; 



</script>

<template>
  <div class="top-line"></div>
  <div class="kiosk-app">
  

<header class="header">
      <div class="header_logo">
        <img src="https://ocsnau.net/wp-content/themes/ocsnau_v3/assets/images/logo_ukr_color.png?v=2" alt="Логотип ОКСНАУ" class="logo-img">
      </div>
      <div class="header_info">
      <h1>Весь коледж на одному екрані</h1>
      </div>
      <div class="header-controls">
        
      </div>
    </header>

    <WellcomeToTheCollege></WellcomeToTheCollege>

   </div>
</template>



<style>
/* Скидання базових стилів для кіоску */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  /* Заборона виділення тексту для touch-екранів */
  user-select: none; 
  -webkit-user-select: none;
}

body {
  font-family: 'Roboto', Tahoma, Geneva, Verdana, sans-serif;
  background-color: #fff; /* Світло-зелений фон */
  color: #064e3b;
  overflow-x: hidden;
}

body {
    background: url(bg.png) no-repeat;
    background-size: cover;
    background-position-y: -35vh;
}

#app {
    background: #ffffffc4;
}


.kiosk-app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  padding: 1rem;

}

.header {
  text-align: center;
  padding-top: 1rem;
  justify-content: space-around;
}

.header h1 {
  font-size: 3rem;
  color: #166534; /* Темно-зелений */
  margin-bottom: 0.5rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.header p {
  font-size: 1.5rem;
  color: #15803d;
}



.tile {
    background: #ffffff94; 
    border-radius: 1em;
    padding: 2rem 1.5rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    cursor: pointer;
    /* box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05); */
    transition: transform 0.15s ease, box-shadow 0.15s ease;
    border: 3px solid #15803d;
}

.tile > img {
  width: 100%;
}

.tile:active {
  transform: scale(0.96);
  border-bottom-width: 2px;
  margin-top: 4px;
}

.tile-code {
  background-color: rgba(255, 255, 255, 0.2);
  padding: 0.25rem 1rem;
  border-radius: 20px;
  font-size: 1.2rem;
  font-weight: bold;
  margin-bottom: 1rem;
}

.tile-title {
  font-size: 1.4rem;
  line-height: 1.3;
  font-weight: 600;
}

/* Модальне вікно */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(6, 78, 59, 0.6); /* Напівпрозорий зелений фон */
  backdrop-filter: blur(8px);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background-color: #ffffff;
  width: 90%;
  border-radius: 24px;
  padding: 3rem;
  position: relative;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
  border-top: 12px solid #16a34a;
}

.close-btn {
  position: absolute;
  top: 1.5rem;
  right: 1.5rem;
  background-color: #f1f5f9;
  color: #334155;
  border: none;
  padding: 1rem 1.5rem;
  border-radius: 12px;
  font-size: 1.2rem;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.2s;
}

.close-btn:active {
  background-color: #e2e8f0;
  transform: scale(0.95);
}

.modal-header {
  margin-bottom: 2rem;
  padding-right: 8rem; /* Щоб текст не налізав на кнопку закриття */
}

.modal-code {
  display: inline-block;
  background-color: #dcfce7;
  color: #166534;
  padding: 0.5rem 1.2rem;
  border-radius: 8px;
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 1rem;
}

.modal-header h2 {
  font-size: 2.5rem;
  color: #064e3b;
  line-height: 1.2;
}

.modal-body p {
  font-size: 1.5rem;
  line-height: 1.6;
  color: #334155;
}

/* Анімації модального вікна */
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

.modal-enter-active .modal-content {
  transition: all 0.3s ease;
}

.modal-enter-from .modal-content {
  transform: translateY(50px) scale(0.95);
}


.top-line {
    height: 8px;
background: #005f47;
    color: #fff;
    }

.bold {
  font-weight: bold;
}

.header {
  display: flex;
    align-content: center;

}
.header_logo img {
  height: 7em;
}

.button {    padding: 8px 20px;
    background-color: #42b983;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: .3s;
}


.tiles-grid {
    -webkit-text-size-adjust: 100%;
    tab-size: 4;
    font-feature-settings: normal;
    font-variation-settings: normal;
    -webkit-tap-highlight-color: transparent;
    line-height: inherit;
    font-family: 'Roboto', sans-serif;
    margin: 0;
    box-sizing: border-box;
    border-width: 0;
    border-style: solid;
    border-color: #e5e7eb;
    margin-left: auto;
    margin-right: auto;
    display: grid;
    width: 100%;
    flex: 1 1 0%;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1.5rem;
    padding: 2rem;
    align-content: start;
    padding-top: 40px;
}

.tile-card {
    -webkit-text-size-adjust: 100%;
    tab-size: 4;
    font-feature-settings: normal;
    font-variation-settings: normal;
    -webkit-tap-highlight-color: transparent;
    line-height: inherit;
    font-family: 'Roboto', sans-serif;
    margin: 0;
    box-sizing: border-box;
    border-width: 0;
    border-style: solid;
    border-color: #e5e7eb;
    transition: transform 0.15s, box-shadow 0.15s;
    cursor: pointer;
    user-select: none;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    border-radius: 1rem;
    padding: 2rem;
    text-align: center;
    --tw-text-opacity: 1;
    color: rgb(255 255 255 / var(--tw-text-opacity, 1));
    background: #00a53f;
    min-height: 180px;
}

.flat-image {
  max-width: 150px;
  filter: invert(100%);
}

.tile-title {
  font-size: 3rem;
  font-weight: bold;
  margin-top: 15px;
  text-transform: uppercase;
}


/* Адаптивність для мобілок */
@media (max-width: 480px) {
  .tiles-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
  }
  
  .tile-title {
    font-size: 1rem;
  }
}


</style>