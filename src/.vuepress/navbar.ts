import { navbar } from "vuepress-theme-hope";

export default navbar([
  "/",
  "/about/",
  {
    text: "Frontend",
    icon: "fa-solid fa-laptop",
    prefix: "frontend/",
    children: ["vue", "vite", "sass", "vuepress", "markdown"],
  },
  {
    text: "Backend",
    icon: "fa-solid fa-server",
    prefix: "backend/",
    children: ["python", "dialogflow"],
  },
]);
