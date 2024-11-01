import { theme as baseTheme } from '@chakra-ui/theme'

const theme = {
  ...baseTheme,
  styles: {
    global: {
      body: {
        bg: 'gray.50',
      },
    },
  },
  colors: {
    ...baseTheme.colors,
    brand: {
      50: '#E5F0FF',
      100: '#B8D5FF',
      200: '#8ABBFF',
      300: '#5CA1FF',
      400: '#2E87FF',
      500: '#006DFF',
      600: '#0057CC',
      700: '#004199',
      800: '#002B66',
      900: '#001533',
    },
  },
}

export default theme
