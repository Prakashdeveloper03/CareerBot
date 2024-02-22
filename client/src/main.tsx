import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.tsx";
import SignupCard from "./components/SignUp.tsx";
import SimpleCard from "./components/SignIn.tsx";
import { ChakraProvider } from "@chakra-ui/react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  },
  {
    path: "/register",
    element: <SignupCard />,
  },
  {
    path: "/login",
    element: <SimpleCard />,
  },
]);

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <ChakraProvider>
      <RouterProvider router={router} />
    </ChakraProvider>
  </React.StrictMode>,
);
