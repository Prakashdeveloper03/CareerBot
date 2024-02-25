import { hopeTheme } from "vuepress-theme-hope";
import navbar from "./navbar.js";
import sidebar from "./sidebar.js";

export default hopeTheme({
  iconAssets: "fontawesome-with-brands",
  logo: "https://theme-hope-assets.vuejs.press/logo.svg",
  docsDir: "src",
  navbar,
  sidebar,
  print: true,
  fullscreen: true,
  darkmode: "toggle",
  footer: "Default footer",
  displayFooter: true,
  encrypt: {
    config: {
      "/demo/encrypt.html": ["1234"],
    },
  },
  metaLocales: {
    editLink: "Edit this page on GitHub",
  },

  plugins: {
    search: true,

    components: {
      components: ["Badge", "VPCard"],
    },

    mdEnhance: {
      align: true,
      attrs: true,
      codetabs: true,
      component: true,
      demo: true,
      figure: true,
      imgLazyload: true,
      imgSize: true,
      include: true,
      stylize: [
        {
          matcher: "Recommended",
          replacer: ({ tag }) => {
            if (tag === "em")
              return {
                tag: "Badge",
                attrs: { type: "tip" },
                content: "Recommended",
              };
          },
        },
      ],
      sub: true,
      sup: true,
      tabs: true,
      vPre: true,
      flowchart: true,
      gfm: true,
      katex: true,
      mathjax: true,
      mermaid: true,
    },
  },
});
