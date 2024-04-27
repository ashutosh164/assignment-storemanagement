<template>
  <div class="px-4 sm:px-6 lg:px-8 py-5">
    <div class="sm:flex sm:items-center">
      <div class="sm:flex-auto">
        <h1 class="text-base font-semibold leading-6 text-gray-900">Inventory</h1>
      </div>
      <div  class="mt-4 sm:ml-16 sm:mt-0 sm:flex-none">
        <button type="button" class="block rounded-md bg-indigo-600 px-3 py-2 text-center text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600" ><NuxtLink to="/add-inventory">Add inventory</NuxtLink></button>
      </div>
    </div>
    <div class="-mx-4 mt-8 sm:-mx-0">
      <table class="min-w-full divide-y divide-gray-300">
        <thead>
          <tr>
            <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-0">Product name</th>
            <th scope="col" class="hidden px-3 py-3.5 text-left text-sm font-semibold text-gray-900 lg:table-cell">vendor</th>
            <th scope="col" class="hidden px-3 py-3.5 text-left text-sm font-semibold text-gray-900 sm:table-cell">Mrp</th>
               <th scope="col" class="hidden px-3 py-3.5 text-left text-sm font-semibold text-gray-900 sm:table-cell">Status</th>
            <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Quantity</th>
            <th scope="col" class="relative py-3.5 pl-3 pr-4 sm:pr-0">
              <span class="sr-only">Edit</span>
            </th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-200 bg-white">
          <tr v-for="item in data" :key="item.id">
            <td class="w-full max-w-0 py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:w-auto sm:max-w-none sm:pl-0">
              {{ item.product_name }}
              <dl class="font-normal lg:hidden">
                <dt class="sr-only">Title</dt>
                <dd class="mt-1 truncate text-gray-700">{{ item.vendor }}</dd>
                <dt class="sr-only sm:hidden">Email</dt>
                <dd class="mt-1 truncate text-gray-500 sm:hidden">{{ item.mrp }}</dd>
              </dl>
            </td>
            <td class="hidden px-3 py-4 text-sm text-gray-500 lg:table-cell">{{ item.vendor }}</td>
            <td class="hidden px-3 py-4 text-sm text-gray-500 lg:table-cell">{{ item.mrp }}</td>

            <!-- <td class="hidden px-3 py-4 text-sm text-gray-500 lg:table-cell">{{ item.quantoty }}</td> -->

            <td class="hidden px-3 py-4 text-sm text-gray-500 sm:table-cell">{{ item.status }}</td>
            <td class="px-3 py-4 text-sm text-gray-500">{{ item.product_id }}</td>
            <td class="py-4 pl-3 pr-4 text-right text-sm font-medium sm:pr-0" >
              <a href="#" class="text-indigo-600 hover:text-indigo-900"><span class="sr-only">, {{ item.batch_num }}</span></a
              >
                <NuxtLink :to="`/add-inventory/${item.id}/`">Edit</NuxtLink>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>




</template>

<script setup>

let response = await fetch(`http://127.0.0.1:8000/inventory/`);
let data = await response.json();
const { inventory } = data;
const is_superuser = ref('')


</script>