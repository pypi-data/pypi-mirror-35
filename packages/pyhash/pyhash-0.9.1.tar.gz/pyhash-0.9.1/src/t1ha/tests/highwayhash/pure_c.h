#ifndef C_HIGHWAYHASH_H_
#define C_HIGHWAYHASH_H_

#include <stdint.h>
#include <string.h>

#if defined(__cplusplus) || defined(c_plusplus)
extern "C" {
#endif

/*////////////////////////////////////////////////////////////////////////////*/
/* Low-level API, use for implementing streams etc...                         */
/*////////////////////////////////////////////////////////////////////////////*/

typedef struct {
  uint64_t v0[4];
  uint64_t v1[4];
  uint64_t mul0[4];
  uint64_t mul1[4];
} HighwayHashState;

/* Initializes state with given key */
static void HighwayHashReset_pure_c(const uint64_t key[4],
                                    HighwayHashState *state);
/* Takes a packet of 32 bytes */
void HighwayHashUpdatePacket_pure_c(const uint8_t *packet,
                                    HighwayHashState *state);
/* Adds the final 1..31 bytes, do not use if 0 remain */
void HighwayHashUpdateRemainder_pure_c(const uint8_t *bytes,
                                       const size_t size_mod32,
                                       HighwayHashState *state);
/* Compute final hash value. Makes state invalid. */
static uint64_t HighwayHashFinalize64_pure_c(HighwayHashState *state);
static void HighwayHashFinalize128_pure_c(HighwayHashState *state,
                                          uint64_t hash[2]);
static void HighwayHashFinalize256_pure_c(HighwayHashState *state,
                                          uint64_t hash[4]);

/*////////////////////////////////////////////////////////////////////////////*/
/* Non-cat API: single call on full data                                      */
/*////////////////////////////////////////////////////////////////////////////*/

uint64_t HighwayHash64_pure_c(const uint64_t key[4], const uint8_t *data,
                              size_t size);

void HighwayHash128_pure_c(const uint64_t key[4], const uint8_t *data,
                           size_t size, uint64_t hash[2]);

void HighwayHash256_pure_c(const uint64_t key[4], const uint8_t *data,
                           size_t size, uint64_t hash[4]);

/*////////////////////////////////////////////////////////////////////////////*/
/* Cat API: allows appending with multiple calls                              */
/*////////////////////////////////////////////////////////////////////////////*/

typedef struct {
  HighwayHashState state;
  uint8_t packet[32];
  size_t num;
} HighwayHashCat;

/* Allocates new state for a new streaming hash computation */
void HighwayHashCatStart_pure_c(const uint64_t key[4], HighwayHashCat *state);

void HighwayHashCatAppend_pure_c(const uint8_t *bytes, size_t num,
                                 HighwayHashCat *state);

/* Computes final hash value */
uint64_t HighwayHashCatFinish64_pure_c(const HighwayHashCat *state);
void HighwayHashCatFinish128_pure_c(const HighwayHashCat *state,
                                    uint64_t hash[2]);
void HighwayHashCatFinish256_pure_c(const HighwayHashCat *state,
                                    uint64_t hash[4]);

/*
Usage examples:

#include <inttypes.h>
#include <stdio.h>

void Example64() {
  uint64_t key[4] = {1, 2, 3, 4};
  const char* text = "Hello world!";
  size_t size = strlen(text);
  uint64_t hash = HighwayHash64((const uint8_t*)text, size, key);
  printf("%016"PRIx64"\n", hash);
}

void Example64Cat() {
  uint64_t key[4] = {1, 2, 3, 4};
  HighwayHashCat state;
  uint64_t hash;

  HighwayHashCatStart(key, &state);

  HighwayHashCatAppend((const uint8_t*)"Hello", 5, &state);
  HighwayHashCatAppend((const uint8_t*)" world!", 7, &state);

  hash = HighwayHashCatFinish64(state);
  printf("%016"PRIx64"\n", hash);
}
*/

#if defined(__cplusplus) || defined(c_plusplus)
} /* extern "C" */
#endif

#endif // C_HIGHWAYHASH_H_
