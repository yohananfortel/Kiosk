<template>
  <section class="contacts-page">
    <header class="contacts-page__header">
      <h2 class="contacts-page__main-title">Контактна інформація</h2>
      <p class="contacts-page__subtitle">
        Відскануйте QR-код для швидкого збереження або переходу
      </p>
    </header>

    <div class="contacts-page__grid">
      <div class="contact-card contact-card--email">
        <div class="contact-card__icon-zone">✉️</div>
        <div class="contact-card__content">
          <span class="contact-card__label">Email</span>
          <div class="contact-card__value">oc_snau@ukr.net</div>
        </div>
        <div class="contact-card__qr-wrapper">
          <img
            src="/img/qr/email.jpg"
            alt="QR Email"
            class="contact-card__qr-image"
          />
          <span class="contact-card__qr-hint">Сканувати Email</span>
        </div>
      </div>

      <div class="contact-card contact-card--phone">
        <div class="contact-card__icon-zone">📞</div>
        <div class="contact-card__content">
          <span class="contact-card__label">Телефон</span>
          <div class="contact-card__value">+38 (05446) 2-20-66</div>
        </div>
        <div class="contact-card__qr-wrapper">
          <img
            src="/img/qr/telephone.jpg"
            alt="QR Telephone"
            class="contact-card__qr-image"
          />
          <span class="contact-card__qr-hint">Сканувати номер</span>
        </div>
      </div>

      <div class="contact-card contact-card--site">
        <div class="contact-card__icon-zone">🌐</div>
        <div class="contact-card__content">
          <span class="contact-card__label">Офіційний сайт</span>
          <div class="contact-card__value">ocsnau.net</div>
        </div>
        <div class="contact-card__qr-wrapper">
          <img
            src="/img/qr/ocsnau.jpg"
            alt="QR Website"
            class="contact-card__qr-image"
          />
          <span class="contact-card__qr-hint">Перейти на сайт</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
// Логіка статична
</script>

<style scoped>
/* =========================================
   Блок: contacts-page (Основний контейнер)
   Методологія: БЕМ
   ========================================= */

.contacts-page {
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

.contacts-page__header {
  text-align: center;
  margin-bottom: 50px;
}

.contacts-page__main-title {
  font-size: 3rem;
  font-weight: 800;
  color: #166534;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin: 0 0 12px 0;
}

.contacts-page__subtitle {
  font-size: 1.35rem;
  color: #64748b;
  margin: 0;
}

/* =========================================
   Елемент: Сітка карток (Повна симетрія)
   ========================================= */
.contacts-page__grid {
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
   Блок: contact-card (Преміум картки контактів)
   ========================================= */
.contact-card {
  width: 360px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 28px;
  padding: 35px 25px;
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
  cursor: default; /* Прибрали курсор-палець для всієї картки, оскільки вона не клікабельна */
}

/* Верхні яскраві кольорові акценти для кожної картки */
.contact-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 8px;
}
.contact-card--email::before {
  background: #00a53f;
}
.contact-card--phone::before {
  background: #3b82f6;
}
.contact-card--site::before {
  background: #f59e0b;
}

/* Інтерактивні ховер-ефекти при дотику/наведенні залишаємо для краси */
.contact-card:hover {
  transform: translateY(-12px);
  background: #ffffff;
  box-shadow: 0 25px 50px rgba(15, 23, 42, 0.08);
}
.contact-card--email:hover {
  border-color: #00a53f;
}
.contact-card--phone:hover {
  border-color: #3b82f6;
}
.contact-card--site:hover {
  border-color: #f59e0b;
}

/* Елемент: Іконка каналу зв'язку */
.contact-card__icon-zone {
  font-size: 3rem;
  margin-bottom: 15px;
  background: #ffffff;
  width: 70px;
  height: 70px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.04);
}

.contact-card__content {
  margin-bottom: 25px;
  flex-grow: 1;
}

/* Елемент: Назва типу контакту */
.contact-card__label {
  display: block;
  font-size: 1.1rem;
  font-weight: 700;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 6px;
}

/* Елемент: Текстове значення контакту (тепер звичайний текст) */
.contact-card__value {
  font-size: 1.6rem;
  font-weight: 800;
  color: #1e293b;
  word-break: break-all;
  line-height: 1.2;
}

/* =========================================
   Елемент: Оформлення рамок для QR-кодів
   ========================================= */
.contact-card__qr-wrapper {
  background: #ffffff;
  border: 2px solid #e2e8f0;
  padding: 15px;
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 170px;
  box-sizing: border-box;
  transition:
    border-color 0.3s ease,
    transform 0.3s ease;
}

.contact-card__qr-image {
  width: 140px;
  height: 140px;
  object-fit: contain;
  margin-bottom: 8px;
}

/* Маленький напис під QR */
.contact-card__qr-hint {
  font-size: 0.85rem;
  font-weight: 700;
  color: #94a3b8;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

/* Анімація збільшення QR при фокусі на картку */
.contact-card:hover .contact-card__qr-wrapper {
  border-color: #cbd5e1;
  transform: scale(1.03);
}
</style>
