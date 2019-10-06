#include <stdio.h>
#include "page.h"

int main(void) {
  const int len = sizeof(ctlPage);
  for (int i = 0; i < len; i++) {
    printf("%c", ctlPage[i] & 0xFF);
  }
  return 0;
}
