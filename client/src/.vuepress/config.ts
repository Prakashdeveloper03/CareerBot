import { defineUserConfig } from "vuepress";
import theme from "./theme.js";

export default defineUserConfig({
  base: "/",
  lang: "en-US",
  title: "CareerBot",
  description: "Course and Job skillset recommendation system",
  theme,
});
