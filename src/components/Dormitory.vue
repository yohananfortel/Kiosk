<template>
    <div class="dormitory">
        <div class="dormitory-content">
            <div class="dormitory-title">
                <h2>Гуртожиток</h2>
            </div>
            <div class="dormitory-info">
                <div class="dormitory-info-item">
                    <div class="dormitory-info-item-title">Адреса</div>
                    <div class="dormitory-info-item-value">вул.Сумська, 43</div>
                </div>
                <div class="dormitory-info-item">
                    <div class="dormitory-info-item-title">Телефон</div>
                    <div class="dormitory-info-item-value">555-55-55</div>
                </div>
                <div class="dormitory-info-item">
                    <div class="dormitory-info-item-title">Email</div>
                    <div class="dormitory-info-item-value">[EMAIL_ADDRESS]</div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.dormitory {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
}
.dormitory-content {
    display: flex;
    flex-direction: column;
    gap: 20px;
}
.dormitory-title {
    text-align: center;
}
.dormitory-title h2 {
    font-size: 3em;
    font-weight: bold;
    color: #00a53f;
}
.dormitory-info {
    display: flex;
    flex-direction: column;
    gap: 20px;
}
.dormitory-info-item {
    display: flex;
    flex-direction: column;
    gap: 10px;
}
.dormitory-info-item-title {
    font-size: 2em;
    font-weight: bold;
}
.dormitory-info-item-value {
    font-size: 2em;
}
</style>