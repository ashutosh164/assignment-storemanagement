const store = useStore()
await useAsyncData('user', () => store.fetchUser().then(() => true))