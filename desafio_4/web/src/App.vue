<template>
  <div class="min-h-screen bg-gray-100 flex flex-col items-center p-6">
    <h1 class="text-3xl font-bold text-gray-800 mb-6">Buscar Operadoras</h1>
    <input type="text" v-model="query" @input="search"
      class="w-full max-w-md p-3 border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
      placeholder="Digite o nome da operadora..." />

    <div v-if="loading" class="mt-4 text-blue-500">Carregando...</div>
    <div v-else-if="error" class="mt-4 text-red-500">Erro ao buscar dados.</div>

    <div v-if="results.length" class="w-full max-w-md mt-6 space-y-4">
      <div v-for="item in results" :key="item.Registro_ANS" class="p-4 bg-white rounded-lg shadow-md border">
        <h2 class="text-lg font-semibold text-gray-700">{{ item.Razao_Social }}</h2>
        <p class="text-gray-500">CNPJ: {{ item.CNPJ }}</p>
        <p class="text-gray-500">Cidade: {{ item.Cidade }}, {{ item.UF }}</p>
        <p class="text-gray-500">Telefone: ({{ item.DDD }}) {{ item.Telefone }}</p>
      </div>
    </div>
    <p v-else-if="query && !loading" class="mt-4 text-gray-500">Nenhum resultado encontrado.</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      query: '',
      results: [],
      loading: false,
      error: false,
    };
  },
  methods: {
    async search() {
      if (this.query.length < 2) {
        this.results = [];
        return;
      }
      this.loading = true;
      this.error = false;
      try {
        const response = await axios.get(`http://localhost:5000/search?q=${this.query}`);
        this.results = response.data;
      } catch (err) {
        this.error = true;
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>
<style>
@import "https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css";
</style>
