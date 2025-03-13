import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import ChallengesList from "./components/ChallengeList";
import { Container } from "@mui/material";

const App: React.FC = () => {
  return (
    <Router>
      <Container>
        <Routes>
          <Route path="/" element={<ChallengesList />} />
        </Routes>
      </Container>
    </Router>
  );
};

export default App;
