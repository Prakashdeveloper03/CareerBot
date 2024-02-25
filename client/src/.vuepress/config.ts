import { defineUserConfig } from "vuepress";
import theme from "./theme.js";

export default defineUserConfig({
  base: "/",
  lang: "en-US",
  title: "Careerbot",
  description: "A documentation for careerbot using vue-press",
  theme
});
