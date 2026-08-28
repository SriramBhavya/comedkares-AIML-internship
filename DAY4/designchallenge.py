<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Movie Ratings Dashboard</title>

  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: Inter, Arial, sans-serif;
    }

    body {
      background: #090b10;
      color: #fff;
      min-height: 100vh;
    }

    .dashboard {
      display: flex;
      min-height: 100vh;
    }

    /* SIDEBAR */
    .sidebar {
      width: 240px;
      background: #11141c;
      border-right: 1px solid #242936;
      padding: 28px 20px;
      position: fixed;
      height: 100vh;
    }

    .logo {
      font-size: 23px;
      font-weight: 800;
      margin-bottom: 45px;
      color: #f5c451;
    }

    .logo span {
      color: #fff;
    }

    .nav-title {
      color: #707787;
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      margin: 25px 0 12px;
    }

    .nav-item {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 12px 14px;
      margin-bottom: 6px;
      border-radius: 9px;
      color: #9da3b0;
      cursor: pointer;
      transition: .2s;
    }

    .nav-item:hover,
    .nav-item.active {
      background: #242936;
      color: #fff;
    }

    .nav-item.active {
      border-left: 3px solid #f5c451;
    }

    /* MAIN */
    .main {
      margin-left: 240px;
      width: calc(100% - 240px);
      padding: 30px;
    }

    .topbar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 30px;
    }

    .heading h1 {
      font-size: 30px;
      margin-bottom: 7px;
    }

    .heading p {
      color: #7f8795;
      font-size: 14px;
    }

    .search {
      background: #151923;
      border: 1px solid #292e3a;
      padding: 12px 16px;
      width: 260px;
      border-radius: 9px;
      color: #fff;
      outline: none;
    }

    .search:focus {
      border-color: #f5c451;
    }

    /* FILTERS */
    .filters {
      display: flex;
      gap: 12px;
      margin-bottom: 25px;
      flex-wrap: wrap;
    }

    select {
      background: #151923;
      color: #ddd;
      border: 1px solid #292e3a;
      padding: 10px 15px;
      border-radius: 8px;
      outline: none;
      cursor: pointer;
    }

    /* KPI */
    .cards {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 18px;
      margin-bottom: 20px;
    }

    .card {
      background: #151923;
      border: 1px solid #242936;
      border-radius: 13px;
      padding: 20px;
    }

    .card-label {
      color: #818896;
      font-size: 13px;
      margin-bottom: 12px;
    }

    .card-value {
      font-size: 30px;
      font-weight: 750;
    }

    .card-change {
      margin-top: 8px;
      color: #53d88a;
      font-size: 12px;
    }

    /* GRID */
    .grid {
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 18px;
      margin-bottom: 18px;
    }

    .panel {
      background: #151923;
      border: 1px solid #242936;
      border-radius: 13px;
      padding: 20px;
    }

    .panel-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
    }

    .panel-header h2 {
      font-size: 16px;
    }

    .panel-header span {
      color: #777f8e;
      font-size: 12px;
    }

    .chart-container {
      height: 290px;
    }

    /* MOVIES */
    .movie {
      display: flex;
      align-items: center;
      gap: 13px;
      padding: 12px 0;
      border-bottom: 1px solid #242936;
    }

    .movie:last-child {
      border-bottom: none;
    }

    .poster {
      width: 45px;
      height: 58px;
      border-radius: 5px;
      object-fit: cover;
      background: #282d38;
    }

    .movie-info {
      flex: 1;
    }

    .movie-title {
      font-size: 13px;
      font-weight: 600;
      margin-bottom: 5px;
    }

    .movie-meta {
      color: #747c8b;
      font-size: 11px;
    }

    .rating {
      color: #f5c451;
      font-weight: 700;
      font-size: 14px;
    }

    /* GENRES */
    .genre {
      margin-bottom: 18px;
    }

    .genre-top {
      display: flex;
      justify-content: space-between;
      font-size: 12px;
      margin-bottom: 7px;
    }

    .genre-rating {
      color: #f5c451;
    }

    .bar {
      width: 100%;
      height: 7px;
      background: #282d38;
      border-radius: 10px;
      overflow: hidden;
    }

    .bar-fill {
      height: 100%;
      background: linear-gradient(90deg, #7067f0, #f5c451);
      border-radius: 10px;
    }

    /* TABLE */
    .table-panel {
      margin-top: 18px;
    }

    table {
      width: 100%;
      border-collapse: collapse;
    }

    th {
      text-align: left;
      color: #737b89;
      font-size: 11px;
      text-transform: uppercase;
      padding: 13px 10px;
      border-bottom: 1px solid #292e39;
    }

    td {
      padding: 15px 10px;
      font-size: 13px;
      border-bottom: 1px solid #202530;
    }

    .star {
      color: #f5c451;
    }

    .up {
      color: #53d88a;
    }

    .down {
      color: #ff6574;
    }

    /* RESPONSIVE */
    @media (max-width: 1100px) {
      .cards {
        grid-template-columns: repeat(2, 1fr);
      }

      .grid {
        grid-template-columns: 1fr;
      }
    }

    @media (max-width: 750px) {
      .sidebar {
        width: 70px;
        padding: 20px 10px;
      }

      .logo {
        font-size: 0;
        text-align: center;
      }

      .logo::after {
        content: "🎬";
        font-size: 22px;
      }

      .nav-item {
        justify-content: center;
        font-size: 0;
      }

      .nav-title {
        display: none;
      }

      .main {
        margin-left: 70px;
        width: calc(100% - 70px);
        padding: 20px;
      }

      .topbar {
        flex-direction: column;
        align-items: flex-start;
        gap: 15px;
      }

      .search {
        width: 100%;
      }

      .cards {
        grid-template-columns: 1fr;
      }

      .table-panel {
        overflow-x: auto;
      }

      table {
        min-width: 650px;
      }
    }
  </style>
</head>

<body>

<div class="dashboard">

  <!-- SIDEBAR -->
  <aside class="sidebar">
    <div class="logo">CINE<span>METRICS</span></div>

    <div class="nav-title">Overview</div>

    <div class="nav-item active">
      📊 <span>Dashboard</span>
    </div>

    <div class="nav-item">
      🎬 <span>Movies</span>
    </div>

    <div class="nav-item">
      ⭐ <span>Ratings</span>
    </div>

    <div class="nav-title">Explore</div>

    <div class="nav-item">
      🎭 <span>Genres</span>
    </div>

    <div class="nav-item">
      📈 <span>Analytics</span>
    </div>
  </aside>


  <!-- MAIN -->
  <main class="main">

    <div class="topbar">
      <div class="heading">
        <h1>Movie Ratings</h1>
        <p>Track, compare and explore movie performance.</p>
      </div>

      <input
        class="search"
        id="search"
        type="text"
        placeholder="🔍 Search movies..."
      />
    </div>


    <!-- FILTERS -->
    <div class="filters">

      <select id="genreFilter">
        <option value="all">All Genres</option>
        <option value="Drama">Drama</option>
        <option value="Sci-Fi">Sci-Fi</option>
        <option value="Action">Action</option>
        <option value="Comedy">Comedy</option>
        <option value="Thriller">Thriller</option>
      </select>

      <select id="yearFilter">
        <option value="all">All Years</option>
        <option value="2024">2024</option>
        <option value="2023">2023</option>
        <option value="2022">2022</option>
        <option value="2021">2021</option>
        <option value="2019">2019</option>
        <option value="2010">2010</option>
      </select>

    </div>


    <!-- KPI CARDS -->
    <section class="cards">

      <div class="card">
        <div class="card-label">Movies Rated</div>
        <div class="card-value" id="movieCount">1,248</div>
        <div class="card-change">↑ 12.4% this month</div>
      </div>

      <div class="card">
        <div class="card-label">Average Rating</div>
        <div class="card-value" id="avgRating">7.6</div>
        <div class="card-change">↑ 0.3 vs last month</div>
      </div>

      <div class="card">
        <div class="card-label">Audience Approval</div>
        <div class="card-value">82%</div>
        <div class="card-change">↑ 4.8% this month</div>
      </div>

      <div class="card">
        <div class="card-label">Total Votes</div>
        <div class="card-value">18.6M</div>
        <div class="card-change">↑ 8.2% this month</div>
      </div>

    </section>


    <!-- CHARTS -->
    <section class="grid">

      <div class="panel">

        <div class="panel-header">
          <h2>Rating Distribution</h2>
          <span>All movies</span>
        </div>

        <div class="chart-container">
          <canvas id="ratingChart"></canvas>
        </div>

      </div>


      <div class="panel">

        <div class="panel-header">
          <h2>Top Rated Movies</h2>
          <span>2024</span>
        </div>

        <div id="movieList"></div>

      </div>

    </section>


    <section class="grid">

      <div class="panel">

        <div class="panel-header">
          <h2>Rating Trends</h2>
          <span>2019 — 2024</span>
        </div>

        <div class="chart-container">
          <canvas id="trendChart"></canvas>
        </div>

      </div>


      <div class="panel">

        <div class="panel-header">
          <h2>Genre Performance</h2>
          <span>Average rating</span>
        </div>

        <div class="genre">
          <div class="genre-top">
            <span>Drama</span>
            <span class="genre-rating">8.1 ★</span>
          </div>
          <div class="bar">
            <div class="bar-fill" style="width: 90%"></div>
          </div>
        </div>

        <div class="genre">
          <div class="genre-top">
            <span>Sci-Fi</span>
            <span class="genre-rating">7.9 ★</span>
          </div>
          <div class="bar">
            <div class="bar-fill" style="width: 87%"></div>
          </div>
        </div>

        <div class="genre">
          <div class="genre-top">
            <span>Animation</span>
            <span class="genre-rating">7.8 ★</span>
          </div>
          <div class="bar">
            <div class="bar-fill" style="width: 84%"></div>
          </div>
        </div>

        <div class="genre">
          <div class="genre-top">
            <span>Thriller</span>
            <span class="genre-rating">7.5 ★</span>
          </div>
          <div class="bar">
            <div class="bar-fill" style="width: 78%"></div>
          </div>
        </div>

        <div class="genre">
          <div class="genre-top">
            <span>Comedy</span>
            <span class="genre-rating">7.2 ★</span>
          </div>
          <div class="bar">
            <div class="bar-fill" style="width: 70%"></div>
          </div>
        </div>

      </div>

    </section>


    <!-- MOVIE TABLE -->
    <section class="panel table-panel">

      <div class="panel-header">
        <h2>Movie Database</h2>
        <span id="resultCount">6 movies</span>
      </div>

      <table>

        <thead>
          <tr>
            <th>Movie</th>
            <th>Year</th>
            <th>Genre</th>
            <th>Rating</th>
            <th>Votes</th>
            <th>Trend</th>
          </tr>
        </thead>

        <tbody id="movieTable"></tbody>

      </table>

    </section>

  </main>

</div>


<script>

  const movies = [
    {
      title: "Inception",
      year: 2010,
      genre: "Sci-Fi",
      rating: 8.8,
      votes: "2.4M",
      trend: "↑",
      poster: "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=100&q=80"
    },
    {
      title: "Parasite",
      year: 2019,
      genre: "Drama",
      rating: 8.5,
      votes: "1.1M",
      trend: "↑",
      poster: "https://images.unsplash.com/photo-1485846234645-a62644f84728?auto=format&fit=crop&w=100&q=80"
    },
    {
      title: "Dune",
      year: 2021,
      genre: "Sci-Fi",
      rating: 8.0,
      votes: "850K",
      trend: "→",
      poster: "https://images.unsplash.com/photo-1440404653325-ab127d49abc1?auto=format&fit=crop&w=100&q=80"
    },
    {
      title: "Oppenheimer",
      year: 2023,
      genre: "Drama",
      rating: 8.6,
      votes: "1.8M",
      trend: "↑",
      poster: "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=100&q=80"
    },
    {
      title: "The Batman",
      year: 2022,
      genre: "Thriller",
      rating: 7.8,
      votes: "980K",
      trend: "↑",
      poster: "https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?auto=format&fit=crop&w=100&q=80"
    },
    {
      title: "Barbie",
      year: 2023,
      genre: "Comedy",
      rating: 7.2,
      votes: "1.3M",
      trend: "→",
      poster: "https://images.unsplash.com/photo-1483909796559-d1f4f7b9a4a1?auto=format&fit=crop&w=100&q=80"
    }
  ];


  const movieList = document.getElementById("movieList");
  const movieTable = document.getElementById("movieTable");
  const search = document.getElementById("search");
  const genreFilter = document.getElementById("genreFilter");
  const yearFilter = document.getElementById("yearFilter");


  function renderMovies() {

    const searchValue = search.value.toLowerCase();
    const genreValue = genreFilter.value;
    const yearValue = yearFilter.value;

    const filtered = movies.filter(movie => {

      const matchesSearch =
        movie.title.toLowerCase().includes(searchValue);

      const matchesGenre =
        genreValue === "all" ||
        movie.genre === genreValue;

      const matchesYear =
        yearValue === "all" ||
        movie.year.toString() === yearValue;

      return matchesSearch && matchesGenre && matchesYear;

    });


    // TABLE
    movieTable.innerHTML = "";

    filtered.forEach(movie => {

      const row = document.createElement("tr");

      row.innerHTML = `
        <td>
          <strong>${movie.title}</strong>
        </td>

        <td>${movie.year}</td>

        <td>${movie.genre}</td>

        <td>
          <span class="star">★</span>
          ${movie.rating}
        </td>

        <td>${movie.votes}</td>

        <td class="${movie.trend === '↑' ? 'up' : ''}">
          ${movie.trend}
        </td>
      `;

      movieTable.appendChild(row);
    });


    // TOP MOVIES
    movieList.innerHTML = "";

    filtered
      .sort((a, b) => b.rating - a.rating)
      .slice(0, 4)
      .forEach(movie => {

        const item = document.createElement("div");

        item.className = "movie";

        item.innerHTML = `
          <img class="poster" src="${movie.poster}" alt="${movie.title}">

          <div class="movie-info">
            <div class="movie-title">
              ${movie.title}
            </div>

            <div class="movie-meta">
              ${movie.year} • ${movie.genre}
            </div>
          </div>

          <div class="rating">
            ★ ${movie.rating}
          </div>
        `;

        movieList.appendChild(item);
      });


    document.getElementById("resultCount").textContent =
      `${filtered.length} movies`;

    document.getElementById("movieCount").textContent =
      filtered.length.toLocaleString();

    if (filtered.length) {

      const avg =
        filtered.reduce((sum, movie) => sum + movie.rating, 0)
        / filtered.length;

      document.getElementById("avgRating").textContent =
        avg.toFixed(1);

    } else {

      document.getElementById("avgRating").textContent = "0.0";

    }

  }


  search.addEventListener("input", renderMovies);
  genreFilter.addEventListener("change", renderMovies);
  yearFilter.addEventListener("change", renderMovies);


  // RATING DISTRIBUTION CHART
  const ratingCtx =
    document.getElementById("ratingChart").getContext("2d");

  new Chart(ratingCtx, {

    type: "bar",

    data: {
      labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],

      datasets: [{
        label: "Movies",
        data: [
          12, 18, 30, 55, 92,
          180, 260, 315, 220, 66
        ],

        backgroundColor: [
          "#393d48",
          "#393d48",
          "#393d48",
          "#393d48",
          "#393d48",
          "#7067f0",
          "#7067f0",
          "#f5c451",
          "#f5c451",
          "#f5c451"
        ],

        borderRadius: 5
      }]
    },

    options: {

      responsive: true,
      maintainAspectRatio: false,

      plugins: {
        legend: {
          display: false
        }
      },

      scales: {

        x: {
          grid: {
            display: false
          },

          ticks: {
            color: "#737b89"
          }
        },

        y: {
          grid: {
            color: "#242936"
          },

          ticks: {
            color: "#737b89"
          }
        }

      }

    }

  });


  // TREND CHART
  const trendCtx =
    document.getElementById("trendChart").getContext("2d");

  new Chart(trendCtx, {

    type: "line",

    data: {

      labels: [
        "2019",
        "2020",
        "2021",
        "2022",
        "2023",
        "2024"
      ],

      datasets: [{

        label: "Average Rating",

        data: [
          7.1,
          7.3,
          7.2,
          7.5,
          7.7,
          7.6
        ],

        borderColor: "#f5c451",

        backgroundColor:
          "rgba(245,196,81,0.08)",

        fill: true,

        tension: 0.4,

        pointBackgroundColor: "#f5c451",

        pointBorderColor: "#f5c451",

        pointRadius: 4

      }]

    },

    options: {

      responsive: true,
      maintainAspectRatio: false,

      plugins: {
        legend: {
          display: false
        }
      },

      scales: {

        x: {
          grid: {
            display: false
          },

          ticks: {
            color: "#737b89"
          }
        },

        y: {

          min: 6,

          max: 9,

          grid: {
            color: "#242936"
          },

          ticks: {
            color: "#737b89"
          }

        }

      }

    }

  });


  renderMovies();

</script>

</body>
</html>
