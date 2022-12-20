import * as React from "react";
import {
  NavLink,
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import {
  AppBar,
  Box,
  Drawer,
  List,
  ListItem,
  ListItemButton,
  ListItemText,
  Toolbar,
  Typography,
} from "@mui/material";
import useMediaQuery from "@mui/material/useMediaQuery";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";
import Setup from "./Routes/Setup";
import Result from "./Routes/Result";
import Pokedex from "./Routes/Pokedex";

function App() {
  const drawerWidth = 240;
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
      <Router>
        <Box sx={{ display: "flex" }}>
          <CssBaseline />
          <AppBar sx={{ zIndex: (theme) => theme.zIndex.drawer + 1 }}>
            <Toolbar>
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
            </Toolbar>
          </AppBar>

          <Drawer
            variant="permanent"
            sx={{
              width: drawerWidth,
              flexShrink: 0,
              [`& .MuiDrawer-paper`]: {
                width: drawerWidth,
                boxSizing: "border-box",
              },
            }}
          >
            <Toolbar />
            <List disablePadding>
              <NavLink
                to={"/"}
                style={{ textDecoration: "none", color: "inherit" }}
              >
                <ListItem>
                  <ListItemButton>
                    <ListItemText>Setup</ListItemText>
                  </ListItemButton>
                </ListItem>
              </NavLink>
              <NavLink
                to={"/pokedex"}
                style={{ textDecoration: "none", color: "inherit" }}
              >
                <ListItem>
                  <ListItemButton>
                    <ListItemText>Pokedex</ListItemText>
                  </ListItemButton>
                </ListItem>
              </NavLink>
            </List>
          </Drawer>
          <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
            <Toolbar />

            <Routes>
              <Route path="/" exact element={<Setup />} />
              <Route path="/result" exact element={<Result />} />
              <Route path="/pokedex" exact element={<Pokedex />} />
            </Routes>
          </Box>
        </Box>
      </Router>
    </ThemeProvider>
  );
}
export default App;
