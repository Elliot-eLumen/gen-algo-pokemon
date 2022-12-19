import * as React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Card } from "@mui/material";
import useMediaQuery from "@mui/material/useMediaQuery";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";
import Setup from "./Routes/Setup";

function App() {
  const prefersDarkMode = useMediaQuery("(prefers-color-scheme: dark)");

  const theme = React.useMemo(
    () =>
      createTheme({
        palette: {
          mode: prefersDarkMode ? "dark" : "light",
        },
      }),
    [prefersDarkMode]
  );

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <Card sx={{ padding: "15px", textAlign: "center" }}>
          <header>Pokemon Team Optimization</header>
        </Card>
        <Routes>
          <Route path="/" exact element={<Setup />} />
        </Routes>
      </Router>
    </ThemeProvider>
  );
}
export default App;
