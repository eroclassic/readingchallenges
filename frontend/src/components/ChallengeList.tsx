import React, { useState, useEffect } from "react";
import { getChallenges } from "../api";
import {
  Container,
  Typography,
  List,
  ListItem,
  ListItemText,
  CircularProgress,
} from "@mui/material";

interface Challenge {
  id: number;
  title: string;
  description: string;
  likes: number;
}

const ChallengeList: React.FC = () => {
  const [challenges, setChallenges] = useState<Challenge[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchData() {
      try {
        console.log("Fetching challenges...");
        const data = await getChallenges();
        console.log("Challenges received:", data);
        setChallenges(data);
      } catch (error) {
        console.error("Error fetching challenges:", error);
      } finally {
        setLoading(false);
      }
    }
    fetchData();
  }, []);

  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Challenges
      </Typography>
      {loading ? (
        <CircularProgress />
      ) : (
        <List>
          {challenges.map((challenge) => (
            <ListItem key={challenge.id}>
              <ListItemText
                primary={challenge.title}
                secondary={challenge.description}
              />
            </ListItem>
          ))}
        </List>
      )}
    </Container>
  );
};

export default ChallengeList;
