"use client";

import { Button, Flex, useColorMode } from "@chakra-ui/react";
import { BsSun, BsMoonStarsFill } from "react-icons/bs";

export default function ColorToggle() {
  const { colorMode, toggleColorMode } = useColorMode();
  return (
    <Flex>
      <Button
        aria-label="Toggle Color Mode"
        onClick={toggleColorMode}
        _focus={{ boxShadow: "none" }}
        w="fit-content"
      >
        {colorMode === "light" ? <BsMoonStarsFill /> : <BsSun />}
      </Button>
    </Flex>
  );
}
