<template>
  <div class="dormitory">
    <header class="dormitory__header">
      <h2 class="dormitory__title">Студентський гуртожиток</h2>
      <p class="dormitory__subtitle">
        Інформація про розташування та контакти адміністрації
      </p>
    </header>

    <div class="dormitory__grid">
      <!-- Адреса -->
      <div class="dormitory-card dormitory-card--address">
        <div class="dormitory-card__icon">
          <svg viewBox="0 0 24 24" width="34" height="34" fill="none" stroke="#166534" stroke-width="2">
            <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z" />
            <circle cx="12" cy="10" r="3" />
          </svg>
        </div>
        <div class="dormitory-card__content">
          <span class="dormitory-card__label">Адреса</span>
          <div class="dormitory-card__value">вул. Сумська, 43</div>
        </div>
      </div>

      <!-- Телефон -->
      <div class="dormitory-card dormitory-card--phone">
        <div class="dormitory-card__icon">
          <svg viewBox="0 0 24 24" width="34" height="34" fill="none" stroke="#3b82f6" stroke-width="2">
            <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z" />
          </svg>
        </div>
        <div class="dormitory-card__content">
          <span class="dormitory-card__label">Черговий / Адміністрація</span>
          <div class="dormitory-card__value">+38 (05446) 2-20-66</div>
        </div>
      </div>

      <!-- Email -->
      <div class="dormitory-card dormitory-card--email">
        <div class="dormitory-card__icon">
          <svg viewBox="0 0 24 24" width="34" height="34" fill="none" stroke="#f59e0b" stroke-width="2">
            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" />
            <polyline points="22,6 12,13 2,6" />
          </svg>
        </div>
        <div class="dormitory-card__content">
          <span class="dormitory-card__label">Електронна пошта</span>
          <div class="dormitory-card__value">oc_snau@ukr.net</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// Інформаційний екран гуртожитку
</script>

<style scoped>
/* ==========================================================================
   Блок: dormitory (Гуртожиток коледжу)
   Методологія: БЕМ
   ========================================================================== */

.dormitory {
  width: 100%;
  min-height: 65vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 20px;
  font-family: system-ui, -apple-system, sans-serif;
  background-color: #ffffff;
}

.dormitory__header {
  text-align: center;
  margin-bottom: 45px;
}

.dormitory__title {
  font-size: 2.8rem;
  font-weight: 800;
  color: #166534;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin: 0 0 10px 0;
}

.dormitory__subtitle {
  font-size: 1.3rem;
  color: #64748b;
  margin: 0;
}

.dormitory__grid {
  display: flex;
  flex-wrap: wrap;
  gap: 35px;
  justify-content: center;
  align-items: stretch;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
}

/* ==========================================================================
   Блок: dormitory-card (Картка гуртожитку)
   ========================================================================== */

.dormitory-card {
  width: 350px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 24px;
  padding: 35px 25px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.04);
  position: relative;
  overflow: hidden;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.dormitory-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 6px;
}

.dormitory-card--address::before { background: #166534; }
.dormitory-card--phone::before { background: #3b82f6; }
.dormitory-card--email::before { background: #f59e0b; }

.dormitory-card:hover {
  transform: translateY(-8px);
  background: #ffffff;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);
}

.dormitory-card__icon {
  font-size: 3rem;
  margin-bottom: 16px;
  background: #ffffff;
  width: 70px;
  height: 70px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.04);
}

.dormitory-card__content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.dormitory-card__label {
  font-size: 1.05rem;
  font-weight: 700;
  color: #64748b;
  text-transform: uppercase;
}

.dormitory-card__value {
  font-size: 1.6rem;
  font-weight: 800;
  color: #1e293b;
  word-break: break-all;
}
</style>
