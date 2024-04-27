<template>

  <div class="flex min-h-full flex-1 flex-col justify-center py-5 sm:px-6 lg:px-8">
   <div class="sm:mx-auto sm:w-full sm:max-w-md ">
   <div class="inline-flex ">
    
      <button type="button" class="block rounded-md bg-indigo-600 px-3 py-2 text-center text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600" @click="openModal">
         <NuxtLink to="/inventory"><--- Go back</NuxtLink>
      </button>
                 <button type="button" @click="deleteInventory()" class="block ml-4 rounded-md bg-red-600 px-3 py-2 text-center text-sm font-semibold text-white shadow-sm hover:bg-red-700 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600" >
         Delete
      </button>
   </div>
      <h2 class="mt-2 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Update inventory</h2>
 
   </div>
   <div class="mt-2 sm:mx-auto sm:w-full sm:max-w-[480px]">
      <div class="bg-white px-6 py-3 shadow sm:rounded-lg sm:px-12">
         <form class="space-y-2" action="#" method="POST">
            <div>
               <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Product Id</label>
               <div class="mt-2">
                  <input id="email" v-model="product_id" name="email" type="number" autocomplete="email" placeholder="product id" required="" class="block w-full rounded-md border-0 px-2 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
               </div>
            </div>
            <div>
               <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Product name</label>
               <div class="mt-2">
                  <input id="email" v-model="product_name" name="email" type="text" placeholder="product name" autocomplete="email" required="" class="block w-full rounded-md border-0 px-2 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
               </div>
            </div>
            <div>
               <label for="email" class="block text-sm font-medium leading-6 text-gray-900">vendor</label>
               <div class="mt-2">
                  <input id="email" v-model="vendor" name="email" placeholder="vendor" type="text" autocomplete="email" required="" class="block w-full rounded-md border-0 px-2 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
               </div>
            </div>
            <div>
               <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Mrp</label>
               <div class="mt-2">
                  <input id="email" v-model="mrp" name="email" placeholder="mrp" type="number" autocomplete="email" required="" class="block w-full rounded-md border-0 px-2 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
               </div>
            </div>
            <div>
                <label for="location" class="block text-sm font-medium leading-6 text-gray-900">Status</label>
                <select id="location" v-model="status" name="location" class="mt-2 block w-full rounded-md border-0 py-1.5 pl-3 pr-10 text-gray-900 ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-indigo-600 sm:text-sm sm:leading-6">
                <option>Approved</option>
                <option selected="">Pending</option>
                </select>
            </div>
            <div>
               <label for="password" class="block text-sm font-medium leading-6 text-gray-900">quantity</label>
               <div class="mt-2">
                  <input v-model="quantity" id="password" name="password" placeholder="quantity" type="number" autocomplete="current-password" required class="block w-full px-2 rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
               </div>
            </div>
            <div>
               <label for="quantity" class="block text-sm font-medium leading-6 text-gray-900">Batch No</label>
               <div class="mt-2">
                  <input v-model="batch_num" id="quantity" placeholder="status" name="password" type="text" autocomplete="current-password" required="" class="block w-full px-2 rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
               </div>
            </div>
            <div>
               <button @click.prevent="updateInventory()" type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Submit</button>
            </div>
         </form>
      </div>
   </div>
</div>
</template>

<script setup>
// import { useStore } from '~/store/store'
const route = useRoute();
const id = route.params.id;

// const store = useStore()

if(process.client) {
    if (localStorage.getItem('is_superuser') == 'true') {
        navigateTo(`/add-inventory/${id}`)
    } else {
      alert("Sorry, You have no authorize to see this page.Please contact with you'r Store manager");
      navigateTo('/inventory')
    }
}


const batch_num = ref('')
const product_id = ref('')
const product_name = ref('')
const quantity = ref('')
const mrp = ref('')
const vendor = ref('')
const status = ref('')

let response = await fetch(`http://127.0.0.1:8000/inventory/${id}/`);
let data = await response.json();
console.log(data)
product_id.value =data.product_id
batch_num.value =data.batch_num
product_name.value =data.product_name
quantity.value =data.quantity
mrp.value =data.mrp
vendor.value =data.vendor
status.value = data.status

async function updateInventory() {
  try {
    const response = await fetch(`http://127.0.0.1:8000/inventory/${id}/`, {
      method: 'PUT',
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json",
      },
      credentials: 'include',
      body: JSON.stringify({
        product_name: product_name.value,
        product_id: product_id.value,
        vendor: vendor.value,
        mrp: mrp.value,
        quantity: quantity.value,
        batch_num: batch_num.value,
        status: status.value,
      }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();

    navigateTo('/inventory');
    console.log(data);
  } catch (error) {
    console.error('An error occurred:', error);
    alert(error)
  }
}

async function deleteInventory() {
       await fetch(`http://127.0.0.1:8000/inventory/${id}/`, {
          method: 'DELETE',
         headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
        credentials: 'include',

        }).then((response) => {
                      navigateTo('/inventory')

              return response.json(); // Parse the JSON response
          })
}

</script>