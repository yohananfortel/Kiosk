<template>
  <div class="dormitory-page">
    <header class="dormitory-page__header">
      <h2 class="dormitory-page__main-title">Гуртожиток</h2>
      <p class="dormitory-page__subtitle">
        Інформація про розташування та контакти адміністрації
      </p>
    </header>

    <div class="dormitory-page__grid">
      <div class="dormitory-card dormitory-card--address">
        <div class="dormitory-card__icon-zone">📍</div>
        <div class="dormitory-card__content">
          <span class="dormitory-card__label">Адреса</span>
          <div class="dormitory-card__value">вул. Сумська, 43</div>
        </div>
      </div>

      <div class="dormitory-card dormitory-card--phone">
        <div class="dormitory-card__icon-zone">📞</div>
        <div class="dormitory-card__content">
          <span class="dormitory-card__label">Телефон</span>
          <div class="dormitory-card__value">555-55-55</div>
        </div>
      </div>

      <div class="dormitory-card dormitory-card--email">
        <div class="dormitory-card__icon-zone">✉️</div>
        <div class="dormitory-card__content">
          <span class="dormitory-card__label">Email</span>
          <div class="dormitory-card__value">oc_snau@ukr.net</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// Компонент статичний, логіку збережено
</script>

<style scoped>
/* =========================================
   Блок: dormitory-page (Основний контейнер)
   Методологія: БЕМ
   ========================================= */

.dormitory-page {
  width: 100%;
  min-height: 70vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 30px 20px;
  box-sizing: border-box;
  font-family:
    system-ui,
    -apple-system,
    sans-serif;
  background-color: #ffffff;
}

.dormitory-page__header {
  text-align: center;
  margin-bottom: 50px;
}

.dormitory-page__main-title {
  font-size: 3rem;
  font-weight: 800;
  color: #166534; /* Фірмовий зелений колір коледжу */
  text-transform: uppercase;
  letter-spacing: 1px;
  margin: 0 0 12px 0;
}

.dormitory-page__subtitle {
  font-size: 1.35rem;
  color: #64748b;
  margin: 0;
}

/* =========================================
   Елемент: Сітка карток (Повна симетрія)
   ========================================= */
.dormitory-page__grid {
  display: flex;
  flex-wrap: wrap;
  gap: 40px;
  justify-content: center;
  align-items: stretch;
  width: 100%;
  max-width: 1250px;
  margin: 0 auto;
}

/* =========================================
   Блок: dormitory-card (Преміум картки)
   ========================================= */
.dormitory-card {
  width: 360px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 28px;
  padding: 40px 25px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  box-sizing: border-box;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.03);
  position: relative;
  overflow: hidden;
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease,
    border-color 0.3s ease;
  cursor: default;
}

/* Верхні яскраві кольорові лінії-акценти для кожної картки */
.dormitory-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 8px;
}
.dormitory-card--address::before {
  background: #00a53f;
}
.dormitory-card--phone::before {
  background: #3b82f6;
}
.dormitory-card--email::before {
  background: #f59e0b;
}

/* Ефекти підстрибування при наведенні/тапі для збереження загального стилю програми */
.dormitory-card:hover {
  transform: translateY(-12px);
  background: #ffffff;
  box-shadow: 0 25px 50px rgba(15, 23, 42, 0.08);
}
.dormitory-card--address:hover {
  border-color: #00a53f;
}
.dormitory-card--phone:hover {
  border-color: #3b82f6;
}
.dormitory-card--email:hover {
  border-color: #f59e0b;
}

/* Елемент: Округла зона під емодзі-іконку */
.dormitory-card__icon-zone {
  font-size: 3rem;
  margin-bottom: 20px;
  background: #ffffff;
  width: 80px;
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.04);
}

.dormitory-card__content {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

/* Елемент: Підпис типу інформації */
.dormitory-card__label {
  display: block;
  font-size: 1.1rem;
  font-weight: 700;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 8px;
}

/* Елемент: Значення (велике, жирне, добре видиме) */
.dormitory-card__value {
  font-size: 1.7rem;
  font-weight: 800;
  color: #1e293b;
  line-height: 1.3;
}
</style>
