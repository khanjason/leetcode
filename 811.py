import collections
class Solution(object):
    def subdomainVisits(self, cpdomains):
        ans = collections.Counter()
        for domain in cpdomains:
            count,domain=domain.split()
            
            count=int(count)
            t=domain.split('.')
            for i in range(len(t)):
                ans[".".join(t[i:])] += count

        return ["{} {}".format(ct, dom) for dom, ct in ans.items()]
