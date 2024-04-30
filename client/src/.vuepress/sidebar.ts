import { sidebar } from "vuepress-theme-hope";

export default sidebar({
  "/": [
    "",
    {
      text: "About",
      icon: "laptop-code",
      prefix: "about/",
      link: "about/",
      children: "structure",
    },
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
  ],
});
