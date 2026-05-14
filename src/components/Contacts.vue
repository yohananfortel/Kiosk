<template>
  <section class="contacts">
    <div class="container">
      <div class="contacts__inner">
        <div class="contacts__content">
          <div class="contacts__email contacts__grid-item">
            <div class="contacts__email-label">Email</div>
            <div class="contacts__email-value">oc_snau@ukr.net</div>
            <div class="contacts__email-qr">
              <img src="/public/img/qr/email.jpg" alt="qr-ocsnau" />
            </div>
          </div>
          <div class="contacts__phone contacts__grid-item">
            <div class="contacts__phone-label">Телефон</div>
            <div class="contacts__phone-value">+38 (05446)2-20-66</div>
            <div class="contacts__phone-qr">
              <img src="/public/img/qr/telephone.jpg" alt="qr-ocsnau" />
            </div>
          </div>
          <div class="contacts__site contacts__grid-item">
            <div class="contacts__site-label">Сайт</div>
            <div class="contacts__site-value">ocsnau.net</div>
            <div class="contacts__site-qr">
              <img src="/public/img/qr/ocsnau.jpg" alt="qr-ocsnau" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts"></script>

<style scoped>
.contacts__grid-item {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-column: span 2;
  text-align: center;
  align-items: center;
}

.contacts__content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
}

.contacts__email,
.contacts__phone,
.contacts__site {
  font-size: 3em;
}

.contacts__site-qr img,
.contacts__phone-qr img,
.contacts__email-qr img {
  width: 50%;
}
</style>
