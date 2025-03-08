import React, { useEffect, useState } from "react";
import api from "../api/axios";

const Home = () => {
  const [data, setData] = useState<any[]>([]);

  useEffect(() => {
    api
      .get("test/")
      .then((res) => setData(res.data.message))
      .catch((err) => console.error(err));
  }, []);

  return <h1>{data}</h1>;
};

export default Home;
