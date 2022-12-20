import * as React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Card, Container, Typography } from "@mui/material";
import useMediaQuery from "@mui/material/useMediaQuery";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";
import Setup from "./Routes/Setup";
import Result from "./Routes/Result";
import Pokedex from "./Routes/Pokedex";

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
      <Card sx={{ borderRadius: "0", padding: "15px 0", marginBottom: 2 }}>
        <Typography
          variant="h6"
          noWrap
          component="a"
          href="/"
          sx={{
            mr: 2,
            pl: 3,
            fontWeight: 700,
            color: "inherit",
            textDecoration: "none",
          }}
        >
          Pokemon Team Optimization
        </Typography>
      </Card>
      <Container maxWidth="100%">
        <Router>
          <Routes>
            <Route path="/" exact element={<Setup />} />
            <Route path="/result" exact element={<Result />} />
            <Route path="/pokedex" exact element={<Pokedex />} />
          </Routes>
        </Router>
      </Container>
    </ThemeProvider>
  );
}
export default App;
