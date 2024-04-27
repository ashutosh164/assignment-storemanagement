<template>
    <NotificationGroup group="top-right">
        <div class="fixed top-0 left-0 right-0 flex items-start justify-end p-6 px-4 py-6 pointer-events-none z-50">
            <div class="w-full max-w-sm">
                <Notification v-slot="{ notifications, close }" enter="ease-out duration-300 transition" enter-from="translate-y-2 opacity-0 sm:translate-y-0 sm:translate-x-4" enter-to="translate-y-0 opacity-100 sm:translate-x-0" leave="transition ease-in duration-500" leave-from="opacity-100" leave-to="opacity-0" move="transition duration-500" move-delay="delay-300">
                    <div v-for="notification in notifications" :key="notification.id" class="w-full max-w-sm mt-4 overflow-hidden bg-white rounded-lg shadow-lg pointer-events-auto ring-1 ring-black ring-opacity-5">
                        <div class="p-4">
                            <div class="flex items-start">
                                <div class="shrink-0">
                                    <Icon name="heroicons:exclamation-circle" class="h-6 w-6 text-red-400" aria-hidden="true" v-if="notification.title == 'Error'" />
                                    <Icon name="heroicons:check-circle" class="h-6 w-6 text-green-400" aria-hidden="true" v-else />
                                </div>
                                <div class="ml-3 w-0 flex-1 pt-0.5">
                                    <p class="font-semibold text-gray-800">
                                        {{ notification.title }}
                                    </p>
                                    <p class="text-sm font-semibold text-gray-500 break-words">
                                        {{ notification.text }}
                                    </p>
                                </div>
                                <div class="flex ml-4 shrink-0">
                                    <button class="inline-flex text-gray-400 bg-white rounded-md hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-400" @click="close(notification.id)">
                                        <Icon name="heroicons:x-mark" class="h-5 w-5" aria-hidden="true" />
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </Notification>
            </div>
        </div>
    </NotificationGroup>

    <NotificationGroup group="bottom-right">
        <div class="fixed bottom-0 right-0 left-0 flex items-start justify-end p-6 px-4 py-6 pointer-events-none z-50">
            <div class="w-full max-w-sm">
                <Notification v-slot="{ notifications, close }" enter="ease-out duration-300 transition" enter-from="translate-y-2 opacity-0 sm:translate-y-0 sm:translate-x-4" enter-to="translate-y-0 opacity-100 sm:translate-x-0" leave="transition ease-in duration-500" leave-from="opacity-100" leave-to="opacity-0" move="transition duration-500" move-delay="delay-300">
                    <div v-for="notification in notifications" :key="notification.id" class="w-full max-w-sm mt-4 overflow-hidden bg-white rounded-lg shadow-lg pointer-events-auto ring-1 ring-black ring-opacity-5">
                        <div class="p-4">
                            <div class="flex items-start">
                                <div class="shrink-0">
                                    <Icon name="heroicons:exclamation-circle" class="h-6 w-6 text-red-400" aria-hidden="true" v-if="notification.title == 'Error'" />
                                    <Icon name="heroicons:check-circle" class="h-6 w-6 text-green-400" aria-hidden="true" v-else />
                                </div>
                                <div class="ml-3 w-0 flex-1 pt-0.5">
                                    <p class="font-semibold text-gray-800">
                                        {{ notification.title }}
                                    </p>
                                    <p class="text-sm font-semibold text-gray-500 break-words">
                                        {{ notification.text }}
                                    </p>
                                </div>
                                <div class="flex ml-8 shrink-0">
                                    <button class="inline-flex text-gray-400 bg-white rounded-md hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-400" @click="close(notification.id)">
                                        <Icon name="heroicons:x-mark" class="h-5 w-5" aria-hidden="true" />
                                    </button>
                                </div>
                            </div>
                            <div class=" ml-9 flex">
                                <router-link :to="{ name: notification.path, params: { id: notification.detail} }">
                                    <!-- <button type="button" class="inline-flex items-center rounded-md border border-transparent bg-indigo-600 px-3 py-2 text-sm font-medium leading-4 text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">{{notification.name}}</button> -->
                                    <button type="button" class="h-8 px-4 m-2 text-sm text-indigo-100 transition-colors duration-150 bg-indigo-700 rounded-lg focus:shadow-outline hover:bg-indigo-800">{{notification.name}}</button>
                                    <button type="button" class="h-8 px-4 m-2 text-sm text-indigo-100 transition-colors duration-150 bg-indigo-700 rounded-lg focus:shadow-outline hover:bg-indigo-800">{{notification.name}}</button>
                                </router-link>
                            </div>
                        </div>
                    </div>
                </Notification>
            </div>
        </div>
    </NotificationGroup>

    <NotificationGroup group="top-left">
        <div class="fixed top-0 left-0 flex items-start justify-end p-6 px-4 py-6 pointer-events-none z-50">
            <div class="w-full ">
                <Notification v-slot="{ notifications, close }" enter="ease-out duration-300 transition" enter-from="translate-y-2 opacity-0 sm:translate-y-0 sm:translate-x-4" enter-to="translate-y-0 opacity-100 sm:translate-x-0" leave="transition ease-in duration-500" leave-from="opacity-100" leave-to="opacity-0" move="transition duration-500" move-delay="delay-300">
                    <div v-for="notification in notifications" :key="notification.id" class="w-full  mt-4  bg-white rounded-lg shadow-lg pointer-events-auto ring-1 ring-black ring-opacity-5">
                        <div class="p-4">
                            <div class="flex items-start">
                                <div class="shrink-0">
                                    <Icon name="heroicons:exclamation-circle" class="h-6 w-6 text-red-400" aria-hidden="true" v-if="notification.title == 'Error'" />
                                    <Icon name="heroicons:check-circle" class="h-6 w-6 text-green-400" aria-hidden="true" v-else />
                                </div>
                                <div class="ml-3 w-full flex-1 pt-0.5">
                                    <p class="font-semibold text-gray-800">
                                        {{ notification.title }}
                                    </p>
                                    <p class="text-sm font-semibold text-gray-500 break-words">
                                        {{ notification.text }}
                                    </p>
                                </div>
                                <div class="flex ml-14 shrink-0">
                                    <button class="inline-flex text-gray-400 bg-white rounded-md hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-400" @click="close(notification.id)">
                                        <Icon name="heroicons:x-mark" class="h-5 w-5" aria-hidden="true" />
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </Notification>
            </div>
        </div>
    </NotificationGroup>

    <NotificationGroup group="bottom-left">
        <div class="fixed bottom-0 left-0 flex items-start justify-end p-6 px-4 py-6 pointer-events-none z-50">
            <div class="w-full max-w-sm">
                <Notification v-slot="{ notifications, close }" enter="ease-out duration-300 transition" enter-from="translate-y-2 opacity-0 sm:translate-y-0 sm:translate-x-4" enter-to="translate-y-0 opacity-100 sm:translate-x-0" leave="transition ease-in duration-500" leave-from="opacity-100" leave-to="opacity-0" move="transition duration-500" move-delay="delay-300">
                    <div v-for="notification in notifications" :key="notification.id" class="w-full max-w-sm mt-4 overflow-hidden bg-white rounded-lg shadow-lg pointer-events-auto ring-1 ring-black ring-opacity-5">
                        <div class="p-4">
                            <div class="flex items-start">
                                <div class="shrink-0">
                                    <Icon name="heroicons:exclamation-circle" class="h-6 w-6 text-red-400" aria-hidden="true" v-if="notification.title == 'Error'" />
                                    <Icon name="heroicons:check-circle" class="h-6 w-6 text-green-400" aria-hidden="true" v-else />
                                </div>
                                <div class="ml-3 w-full flex-1 pt-0.5">
                                    <p class="font-semibold text-gray-800">
                                        {{ notification.title }}
                                    </p>
                                    <p class="text-sm font-semibold text-gray-500 break-words">
                                        {{ notification.text }}
                                    </p>
                                </div>
                                <div class="flex ml-14 shrink-0">
                                    <button class="inline-flex text-gray-400 bg-white rounded-md hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-400" @click="close(notification.id)">
                                        <Icon name="heroicons:x-mark" class="h-5 w-5" aria-hidden="true" />
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </Notification>
            </div>
        </div>
    </NotificationGroup>
</template>

<script setup>

</script>