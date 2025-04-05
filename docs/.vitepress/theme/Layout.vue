<script setup lang="ts">
import DefaultTheme from "vitepress/theme";
import { useData, inBrowser } from "vitepress";
import { watchEffect, nextTick } from "vue";
import { useRoute } from "vitepress/client";
import ClientOnly from "./ClientOnly.vue";
const route = useRoute();

const loadGoogleTranslate = () => {
  nextTick(() => {
    import("./ClientOnly.vue").then((module) => {
      if (typeof window !== "undefined") {
        const script = document.createElement("script");
        script.src = "https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit";
        script.async = true;
        document.body.appendChild(script);

        window.googleTranslateElementInit = function () {
          new window.google.translate.TranslateElement(
            { pageLanguage: "th", includedLanguages: "en,th" },
            "google_translate_element"
          );
        };
      }
    });
  });
};

watchEffect(() => {
  loadGoogleTranslate();
});
</script>

<template>
  <div class="translate-wrapper">
    <div id="google_translate_element"></div>
  </div>
  <DefaultTheme.Layout />
</template>

<style>
/* Wrapper for positioning */
.translate-wrapper {
  position: fixed;
  top: 60px;
  right: 20px;
  z-index: 1000;
}

#google_translate_element select {
  width: 120px;
  padding: 5px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

iframe {
  bottom: 0 !important;
  top: initial !important;
}
</style>
