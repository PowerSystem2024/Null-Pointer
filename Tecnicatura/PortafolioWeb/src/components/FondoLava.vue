<script>
</script>
<template>
    <svg preserveAspectRatio="xMidYMid slice" viewBox="10 10 80 80">
        <defs>
            <!-- Nuevos gradientes de color -->
            <linearGradient id="gradient1" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#4b6cb7;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#182848;stop-opacity:1" />
            </linearGradient>
            <linearGradient id="gradient2" x1="100%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#3a7bd5;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#00d2ff;stop-opacity:1" />
            </linearGradient>
            <linearGradient id="gradient3" x1="100%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#11998e;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#38ef7d;stop-opacity:1" />
            </linearGradient>
        </defs>

        <!-- Nuevas formas con gradientes actualizados -->
        <path fill="url(#gradient1)" class="out-top"
            d="M45-5C30-18,2-19-8-5c-10,14,3,38,22,50C48,60,75,30,60,10C50-10,60-5,45-5Z" />
        <path fill="url(#gradient2)" class="in-top"
            d="M15,15C10,8,0,10-5,25c-8,18,5,40,20,35S35,25,25,15Z" />
        <path fill="url(#gradient3)" class="out-bottom"
            d="M90,55c-10-5-25-2-35,8c-15,20-20,60,0,75s55,10,65-10c8-15,5-40-5-55C110,60,100,60,90,55Z" />
        <path fill="url(#gradient2)" class="in-bottom"
            d="M85,70c-10-4-20,2-30,10c-12,15-15,45,0,50c15,5,40-10,45-30C105,85,95,75,85,70Z" />
    </svg>
</template>

<style scoped>
/* Nuevas animaciones: rotación, pulso y traslación */
@keyframes rotate {
    0% { transform: rotate(0deg) translateX(0px); }
    50% { transform: rotate(180deg) translateX(10px); }
    100% { transform: rotate(360deg) translateX(0px); }
}

@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.1); }
}

@keyframes oscillate {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-5px); }
    100% { transform: translateY(0px); }
}

/* Aplicación de animaciones y sombras */
.out-top {
    animation: rotate 18s linear infinite, pulse 4s ease-in-out infinite;
    transform-origin: 15px 25px;
    filter: drop-shadow(0 8px 15px rgba(0, 0, 0, 0.3));
}

.in-top {
    animation: oscillate 5s ease-in-out infinite, rotate 25s linear infinite;
    transform-origin: 13px 30px;
    filter: drop-shadow(0 5px 10px rgba(0, 0, 0, 0.25));
}

.out-bottom {
    animation: rotate 22s linear infinite, pulse 6s ease-in-out infinite;
    transform-origin: 90px 95px;
    filter: drop-shadow(0 8px 15px rgba(0, 0, 0, 0.3));
}

.in-bottom {
    animation: oscillate 6s ease-in-out infinite, rotate 15s linear infinite;
    transform-origin: 85px 90px;
    filter: drop-shadow(0 8px 15px rgba(0, 0, 0, 0.35));
}

/* Ajuste SVG y fondo */
svg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    border-radius: 10px;
    overflow: hidden;
    background-color: #1e3c72;
}
</style>
