# Maintainer: Konstantin Shalygin (k0ste@opentech.ru)

pkgname='lcdtester'
pkgver='0.1'
pkgrel='0'
pkgdesc='Perfrom dead pixel test on Python'
arch=('any')
url='https://github.com/codebrainz/lcdtester'
depends=('python2' 'python2-pygame')
makedepends=('git')
license=('GPL')
source=("git://github.com/k0ste/lcdtester.git" 'lcdtest.install')
install=('lcdtest.install')
sha256sums=('SKIP' 'defef6925a9443cfaeb2f1ea96f9a789befd35346fca446ba9b0bade472b88fe')

package() {
  pushd "$pkgname"
  for icon in 16 32 48 64 128 256; do
    install -Dm644 "lcd-$icon.png" \
    "$pkgdir/usr/share/icons/hicolor/${icon}x${icon}/apps/lcdtest.png"
  done
  install -Dm755 "lcdtest.py" "$pkgdir/usr/bin/lcdtest.py"
  install -Dm644 "lcdtest.desktop" "$pkgdir/usr/share/applications/lcdtest.desktop"
  popd
}
